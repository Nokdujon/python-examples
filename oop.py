"""Object Oriented Programming"""


class Student:
    """Class encapsulation"""

    def __init__(self, given_name: str, given_age: int):
        """
        self._a is a protected member and can be accessed by the class and its subclasses.
        Private members in Python are conventionally used with preceding double
        underscores: __. self.__b is a private member of the class Alpha and
        can only be accessed from within the class Alpha.
        """
        self._name: str = given_name  # Protected member ‘name’
        self.__age: int = given_age  # Private member ‘age’


def name_mangling() -> None:
    """Function demonstrates name mangling
    It should be noted that these private and protected members can still be
    accessed from outside of the class by using public methods to access them
    or by a practice known as name mangling. Name mangling is the use of two
    leading underscores and one trailing underscore, for example:

    _class__identifier
    Class is the name of the class and identifier is the data member that I want to access."""

    s1 = Student("Santhosh", 21)
    print(s1._Student__age)


class SuperClass:
    """Class method overriding
    Python code to illustrate how mangling works
    With method overriding"""

    def __init__(self):
        self.__private()
        self._protected()
        self.public()

    def __private(self):
        print("private: SuperClass")

    def _protected(self):
        print("protected: SuperClass")

    def public(self):
        print("public: SuperClass")

    # private copy of original public() method
    __public = public


class SubClass(SuperClass):
    """Class
    provides new signature for public() but does not break __init__()"""

    def public(self):
        print("public: In SubClass")


def method_overriding() -> None:
    """Function demonstrates method overriding"""
    super_class_obj = SuperClass()
    sub_class_obj = SubClass()
    super_class_obj.public()  # public: SuperClass
    sub_class_obj.public()  # public: In SubClass
    sub_class_obj._SuperClass__public()  # public: SuperClass


def polymorphism() -> None:
    """Function demonstrates polymorphism"""

    # In the example, the same operator () to perform on a string, integer and
    # a list. The () operator behaves differently in all three cases.
    string = "poly"
    sequence = [1, 2, 3]
    print(len(string))  # 4
    print(len(sequence))  # 3
