import mlflow
import pickle
import pandas as pd


class DataLeakageRetrospective:

    def __init__(self, pipeline_run):
        self.pipeline_run = pipeline_run
        self.mlflow_run = mlflow.get_run(run_id=pipeline_run.run.info.run_id)

    def compute_leaked_tuples(self):
        path = f'{self.mlflow_run.info.artifact_uri}/{self.mlflow_run.data.tags["arguseyes.data_leakage.provenance_file"]}'

        with open(path, 'rb') as handle:
            leaked_tuples_provenance = pickle.load(handle)

        inputs_required = set()
        for polynomial in leaked_tuples_provenance:
            for elem in polynomial:
                inputs_required.add(elem.operator_id)

        if len(inputs_required) == 1:
            leaked_tuple_ids = []
            for polynomial in leaked_tuples_provenance:
                for elem in polynomial:
                    leaked_tuple_ids.append(elem.row_id)

            input_index = list(inputs_required)[0]
            return self.load_partial_tuples(input_index, leaked_tuple_ids)

        else:

            partials = []

            for input_index in inputs_required:
                leaked_tuple_ids = []
                for polynomial in leaked_tuples_provenance:
                    for elem in polynomial:
                        if elem.operator_id == input_index:
                            leaked_tuple_ids.append(elem.row_id)

                partial_data = self.load_partial_tuples(input_index, leaked_tuple_ids)
                partials.append(partial_data)

            combined = pd.concat(partials, axis=1)
            # TODO this is based on duplicate column names only, should also check column contents
            combined = combined.loc[:, ~combined.columns.duplicated()].copy()
            return combined

    def load_partial_tuples(self, input_index, leaked_tuple_ids):
        data = self.pipeline_run.load_input_with_provenance(input_index)

        data['row_id'] = data.apply(lambda row: row['mlinspect_lineage'][0]['row_id'], axis=1)
        ids = pd.DataFrame.from_dict({'row_id': leaked_tuple_ids})

        partial_tuples = ids.merge(data, on='row_id')
        partial_tuples = partial_tuples.drop(columns=['row_id', 'mlinspect_lineage'])

        return partial_tuples

