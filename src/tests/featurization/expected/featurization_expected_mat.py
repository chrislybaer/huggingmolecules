from huggingmolecules.featurization.featurization_mat import MatBatchEncoding, MatMoleculeEncoding
from numpy.ma import array
from torch import FloatTensor

expected_encoded_smiles = [
    MatMoleculeEncoding(
        node_features=array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                              0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1.,
                              0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0.,
                              0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0.,
                              0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1.,
                              0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.]]),
        adjacency_matrix=array([[0., 0., 0., 0., 0.],
                                [0., 1., 1., 0., 0.],
                                [0., 1., 1., 1., 0.],
                                [0., 0., 1., 1., 1.],
                                [0., 0., 0., 1., 1.]]),
        distance_matrix=array([[1.00000000e+06, 1.00000000e+06, 1.00000000e+06, 1.00000000e+06, 1.00000000e+06],
                               [1.00000000e+06, 0.00000000e+00, 1.49726296e+00, 2.46955618e+00, 3.85851039e+00],
                               [1.00000000e+06, 1.49726296e+00, 0.00000000e+00, 1.33899509e+00, 2.46955663e+00],
                               [1.00000000e+06, 2.46955618e+00, 1.33899509e+00, 0.00000000e+00, 1.49726289e+00],
                               [1.00000000e+06, 3.85851039e+00, 2.46955663e+00, 1.49726289e+00, 0.00000000e+00]]),
        y=None),
    MatMoleculeEncoding(
        node_features=array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                              0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0.,
                              0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0.,
                              0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.]]),
        adjacency_matrix=array([[0., 0., 0.],
                                [0., 1., 1.],
                                [0., 1., 1.]]),
        distance_matrix=array([[1.00000000e+06, 1.00000000e+06, 1.00000000e+06],
                               [1.00000000e+06, 0.00000000e+00, 1.21945472e+00],
                               [1.00000000e+06, 1.21945472e+00, 0.00000000e+00]]),
        y=None)]

expected_batch = MatBatchEncoding(
    node_features=FloatTensor([[[1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                                 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1.,
                                 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                                [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0.,
                                 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                                [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0.,
                                 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                                [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1.,
                                 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.]],

                               [[1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                                 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0.,
                                 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                                [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0.,
                                 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                                [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                                 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                                 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]]),
    adjacency_matrix=FloatTensor([[[0., 0., 0., 0., 0.],
                                   [0., 1., 1., 0., 0.],
                                   [0., 1., 1., 1., 0.],
                                   [0., 0., 1., 1., 1.],
                                   [0., 0., 0., 1., 1.]],

                                  [[0., 0., 0., 0., 0.],
                                   [0., 1., 1., 0., 0.],
                                   [0., 1., 1., 0., 0.],
                                   [0., 0., 0., 0., 0.],
                                   [0., 0., 0., 0., 0.]]]),
    distance_matrix=FloatTensor([[[1.0000e+06, 1.0000e+06, 1.0000e+06, 1.0000e+06, 1.0000e+06],
                                  [1.0000e+06, 0.0000e+00, 1.4973e+00, 2.4696e+00, 3.8585e+00],
                                  [1.0000e+06, 1.4973e+00, 0.0000e+00, 1.3390e+00, 2.4696e+00],
                                  [1.0000e+06, 2.4696e+00, 1.3390e+00, 0.0000e+00, 1.4973e+00],
                                  [1.0000e+06, 3.8585e+00, 2.4696e+00, 1.4973e+00, 0.0000e+00]],

                                 [[1.0000e+06, 1.0000e+06, 1.0000e+06, 0.0000e+00, 0.0000e+00],
                                  [1.0000e+06, 0.0000e+00, 1.2195e+00, 0.0000e+00, 0.0000e+00],
                                  [1.0000e+06, 1.2195e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
                                  [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
                                  [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]]]),
    y=None, batch_size=2)
