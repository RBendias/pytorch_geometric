import copy
from typing import Any, Dict, List, Optional, Tuple, Union

from torch import Tensor
from torch_sparse import SparseTensor

# Types for accessing data ####################################################

# Node-types are denoted by a single string, e.g.: `data['paper']`:
NodeType = str

# Edge-types are denotes by a triplet of strings, e.g.:
# `data[('author', 'writes', 'paper')]
EdgeType = Tuple[str, str, str]

# There exist some short-cuts to query edge-types (given that the full triplet
# can be uniquely reconstructed, e.g.:
# * via str: `data['writes']`
# * via Tuple[str, str]: `data[('author', 'paper')]`
QueryType = Union[NodeType, EdgeType, str, Tuple[str, str]]

Metadata = Tuple[List[NodeType], List[EdgeType]]

# Types for message passing ###################################################

Adj = Union[Tensor, SparseTensor]
OptTensor = Optional[Tensor]
PairTensor = Tuple[Tensor, Tensor]
OptPairTensor = Tuple[Tensor, Optional[Tensor]]
PairOptTensor = Tuple[Optional[Tensor], Optional[Tensor]]
Size = Optional[Tuple[int, int]]
NoneType = Optional[Tensor]

# Types for sampling ##########################################################

InputNodes = Union[OptTensor, NodeType, Tuple[NodeType, OptTensor]]

# Helper functions ############################################################


def map_annotation(annotation: Any, mapping: Dict[Any, Any]) -> Any:
    if getattr(annotation, '__origin__', None) == Union:
        args = getattr(annotation, '__args__', [])
        out = copy.copy(annotation)
        setattr(out, '__args__', [map_annotation(a, mapping) for a in args])
        return out
    elif annotation in mapping:
        return mapping[annotation]
    return annotation
