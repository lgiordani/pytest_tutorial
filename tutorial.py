# TEST Import and instantiate

from dictregister import dictregister as dr


def test_init():
    dr.DictRegister()

##########################################

# TEST test_mutable_sequence()

import collections


def test_mutable_sequence():
    assert isinstance(dr.DictRegister(), collections.MutableSequence)

##########################################

# TEST test_append_works()


def test_append_works():
    d = dr.DictRegister()

    d.append({'a': 1, 'b': 2})

    assert len(d) == 1
    assert d[0] == {'a': 1, 'b': 2}

##########################################

# TEST test_append_checks_if_mapping()

import pytest


def test_append_checks_if_mapping():
    d = dr.DictRegister()

    d.append({'a': 1, 'b': 2})

    with pytest.raises(TypeError):
        d.append([1, 2, 3, 4])

##########################################

# TEST test_init_with_list_of_dicts()


def simple_dict():
    return {'a': 1, 'b': 2}


def test_init_with_list_of_dicts(simple_dict):
    d = dr.DictRegister([simple_dict])

    assert len(d) == 1

##########################################

# TEST test_find_single_key()


def test_find_single_key():
    d = dr.DictRegister([
        {'a': 1, 'b': 2},
        {'a': 5, 'c': 6},
        {'b': 3, 'c': 9}
    ])

    assert d.find('a') == dr.DictRegister([{'a': 1, 'b': 2}, {'a': 5, 'c': 6}])

##########################################

# TEST test_find_multiple_keys()


def test_find_multiple_keys():
    d = dr.DictRegister([
        {'a': 1, 'b': 2},
        {'a': 5, 'c': 6},
        {'b': 3, 'c': 9}
    ])

    assert d.find('a', 'b') == dr.DictRegister([{'a': 1, 'b': 2}])

##########################################

# TEST test_find_single_key_value()


def test_find_single_key_value():
    d = dr.DictRegister([
        {'a': 1, 'b': 2},
        {'a': 5, 'c': 6},
        {'b': 3, 'c': 9}
    ])

    assert d.find(a=1) == dr.DictRegister([{'a': 1, 'b': 2}])

##########################################

# TEST test_find_single_key_value_multiple_results()


def test_find_single_key_value_multiple_results():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find(c=4) == dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4}
    ])

##########################################

# TEST test_find_multiple_key_values()


def test_find_multiple_key_values():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find(a=1, c=4) == dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4}
    ])

##########################################

# TEST test_find_unnamed_and_named()


def test_find_unnamed_and_named():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find('a', b=6) == dr.DictRegister([
        {'a': 5, 'b': 6, 'c': 4}
    ])

##########################################

# TEST test_find_explicit_equal()


def test_find_explicit_equal():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find(b__eq=6) == dr.DictRegister([
        {'a': 5, 'b': 6, 'c': 4}
    ])

##########################################

# TEST test_find_greater_than() [uncommented]


def test_find_greater_than():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find(b__gt=3) == dr.DictRegister([
        {'a': 5, 'b': 6, 'c': 4}
    ])

##########################################

# find() refactoring

##########################################

# TEST test_add_keyword()


def test_add_keyword():
    d = dr.DictRegister([{'x': 1, 'y': 2}, {'x': 3, 'y': 4}])
    d.kadd('z', 3)

    assert len(d) == 2
    assert d == dr.DictRegister(
        [{'x': 1, 'y': 2, 'z': 3}, {'x': 3, 'y': 4, 'z': 3}])

##########################################

# TEST test_remove_keyword()


def test_remove_keyword():
    d = dr.DictRegister([{'x': 1, 'y': 2}, {'x': 3, 'y': 4}])
    d.kremove('x')

    assert len(d) == 2
    assert d == dr.DictRegister([{'y': 2}, {'y': 4}])

##########################################

# TEST test_remove_not_present_keyword()


def test_remove_not_present_keyword():
    d = dr.DictRegister([{'x': 1, 'y': 2, 'z': 8}, {'x': 3, 'y': 4}])
    d.kremove('z')

    assert len(d) == 2
    assert d == dr.DictRegister([{'x': 1, 'y': 2}, {'x': 3, 'y': 4}])

##########################################

# TEST test_add_already_present_keyword()


def test_add_already_present_keyword():
    d = dr.DictRegister([{'x': 1, 'y': 2}])
    d.kadd('x', 3)

    assert len(d) == 1
    assert d == dr.DictRegister([{'x': {1, 3}, 'y': 2}])

##########################################

# TEST test_remove_keyword_with_value()


def test_remove_keyword_with_value():
    d = dr.DictRegister([{'x': 5, 'y': 2}, {'x': 3, 'y': 4}])
    d.kremove('y', 2)

    assert len(d) == 2
    assert d == dr.DictRegister([{'x': 5}, {'x': 3, 'y': 4}])

##########################################

# TEST test_remove_keyword_value_from_multiple_values()


def test_remove_keyword_value_from_multiple_values():
    d = dr.DictRegister([{'x': {5, 6}, 'y': 2}, {'x': 3, 'y': 4}])
    d.kremove('x', 5)

    assert len(d) == 2
    assert d == dr.DictRegister([{'x': 6, 'y': 2}, {'x': 3, 'y': 4}])

##########################################

# TEST test_remove_keyword_value_not_present_from_multiple_values()


def test_remove_keyword_value_not_present_from_multiple_values():
    d = dr.DictRegister([{'x': {2, 6}, 'y': 2}, {'x': 3, 'y': 4}])
    d.kremove('x', 5)

    assert len(d) == 2
    assert d == dr.DictRegister([{'x': {2, 6}, 'y': 2}, {'x': 3, 'y': 4}])

##########################################
