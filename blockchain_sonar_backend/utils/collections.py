from typing import Optional, Sequence, Type, TypeVar

T = TypeVar("T")
S = TypeVar("S")

def filter_type_single(type: Type[T], items: Sequence[S]) -> T:
	filter_instance: filter = filter(lambda x: isinstance(x, type), items)
	single_item = next(filter_instance)
	try:
		next(filter_instance)
	except(StopIteration):
		return single_item
	raise Exception("Three more then one item returned by filter predicate")

def filter_type_single_or_none(type: Type[T], items: Sequence[S]) -> Optional[T]:
	filter_instance: filter = filter(lambda x: isinstance(x, type), items)
	try:
		single_item = next(filter_instance)
	except(StopIteration):
		return None
	try:
		next(filter_instance)
	except(StopIteration):
		return single_item
	raise Exception("Three more then one item returned by filter predicate")



