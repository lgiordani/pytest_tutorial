# CODE Import and instantiate

class DictRegister:
    pass

##########################################

# CODE test_mutable_sequence()

class DictRegister(list):
    pass

##########################################

# CODE test_append_checks_if_mapping() [not working]

import collections


class DictRegister(list):

    def append(self, elem):
        if not isinstance(elem, collections.Mapping):
            raise TypeError


# CODE test_append_checks_if_mapping()

class DictRegister(list):
    def append(self, elem):
        if not isinstance(elem, collections.Mapping):
            raise TypeError
        super().append(elem)


##########################################

# CODE test_find_single_key()

    def find(self, key):
        return self.__class__(
            [d for d in self if key in d]
        )

##########################################

# CODE test_find_multiple_keys()

    def find(self, *args):
        return self.__class__(
            [d for d in self if set(args).issubset(set(d.keys()))]
        )

##########################################

# CODE test_find_single_key_value()

    def find(self, *args, **kwargs):
        args_result = self.__class__(
            [d for d in self if set(args).issubset(set(d.keys()))]
        )

        return self.__class__(
            [d for d in args_result if kwargs.items() <= d.items()]
        )

##########################################

# CODE test_find_explicit_equal()

    def find(self, *args, **kwargs):
        result = self.__class__(
            [d for d in self if set(args).issubset(set(d.keys()))]
        )
 
        norm_kwargs = {}
        for k, v in kwargs.items():
            if '__' not in k:
                k = k + '__eq'
            norm_kwargs[k] = v

        for k, v in norm_kwargs.items():
            key, operator = k.split('__')
            if operator == 'eq':
                result = [d for d in result if key in d and d[key] == v]

        return self.__class__(result)

##########################################

# CODE test_find_greater_than()

            elif operator == 'gt':
                result = [d for d in result if key in d and d[key] > v]

##########################################

# CODE find() refactoring

    def _match(self, item, keyop, value):
        # Split key and operator
        if '__' not in keyop:
            keyop = keyop + '__eq'
        key, op = keyop.split('__')

        if op == "eq":
            try:
                return item[key] == value
            except KeyError:
                return False
        else:
            return item[key] > value

    def find(self, *args, **kwds):
        starting_list = self.__class__(
            [d for d in self if set(args).issubset(set(d.keys()))]
        )
 
        filtered_list = []
        for key, value in kwds.items():
            for item in starting_list:
                if self._match(item, key, value):
                    filtered_list.append(item)
            starting_list = filtered_list
            filtered_list = []

        return self.__class__(starting_list)

##########################################

# CODE test_add_keyword()

    def kadd(self, key, value):
        for item in self:
            item[key] = value


##########################################

# CODE test_remove_keyword()

    def kremove(self, key):
        for item in self:
            item.pop(key)


##########################################

# CODE test_remove_not_present_keyword()

    def kremove(self, key):
        for item in self:
            item.pop(key, None)


##########################################

# CODE test_add_already_present_keyword()

   def kadd(self, key, value):
        for item in self:
           try:
               # Use the key as a set
               item[key].add(value)
           except KeyError:
               # This happens if the key is not present
               item[key] = value
           except AttributeError:
               # This happens if the key is present but is not a set
               item[key] = set([item[key], value])
                

##########################################

# CODE test_remove_keyword_with_value()


    def kremove(self, key, value=None):
        for item in self:
            if value is None:
                item.pop(key, None)
            else:
                if item[key] == value:
                    item.pop(key)


##########################################

# CODE test_remove_keyword_value_from_multiple_values()

    def kremove(self, key, value=None):
        for item in self:
            if value is None:
                # Just pop the key if present,
                # otherwise return None
                # (shortcut to ignore the exception)
                item.pop(key, None)
            else:
                try:
                    # Use the key as a set
                    item[key].remove(value)
                    # If the set contains a single element
                    # just store the latter
                    if len(item[key]) == 1:
                        item[key] = item[key].pop()
                except AttributeError:
                    # This happens when the key is not a set
                    # and shall be removed only if values match
                    if item[key] == value:
                        item.pop(key)

##########################################

# CODE test_remove_keyword_value_not_present_from_multiple_values()

                except KeyError:
                    # This happens when the item
                    # does not contain the key
                    pass
                except AttributeError:
                    # This happens when the key is not a set
                    # and shall be removed only if values match
                    if item[key] == value:
                        item.pop(key)


##########################################
