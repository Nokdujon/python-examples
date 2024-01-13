"""Object Oriented Programming"""


class Student:
    """Class encapsulation"""

    def __init__(self, given_name: str, given_age: int) -> None:
        """
        self._a is a protected member and can be accessed by the class and its subclasses.
        Private members in Python are conventionally used with preceding double
        underscores: __. self.__b is a private member of the class Alpha and
        can only be accessed from within the class Alpha.
        """
        self._name: str = given_name  # Protected member ‘name’
        self.__age: int = given_age  # Private member ‘age’
        self.show()

    def show(self) -> None:
        """Function showing a student's properties"""
        print(self._name)
        print(self.__age)

    def get_name(self) -> str:
        """Function retruning a student's name"""
        return self._name

    def get_age(self) -> int:
        """Function returning a student's age"""
        return self.__age


def name_mangling() -> None:
    """Function demonstrates name mangling
    It should be noted that these private and protected members can still be
    accessed from outside of the class by using public methods to access them
    or by a practice known as name mangling. Name mangling is the use of two
    leading underscores and one trailing underscore, for example:

    _class__identifier
    Class is the name of the class and identifier is the data member that I want to access."""

    s1 = Student("Santhosh", 21)

    # Accessing a protected member
    print(f"s1._name = {s1._name}")  # s1._name = Santhosh
    print(f"s1.get_name() = {s1.get_name()}")  # s1.get_name() = Santhosh

    # Accessing a private member
    print(f"s1.get_age() = {s1.get_age()}")  # s1.get_age() = 21
    print(f"s1._Student__age = {s1._Student__age}")  # s1._Student__age = 21
    print(
        f"s1.__age = {s1.__age}"
    )  # AttributeError: 'Student' object has no attribute '__age'.


class SuperClass:
    """Class method overriding
    Python code to illustrate how mangling works
    With method overriding"""

    def __init__(self, fruit: str) -> None:
        self.__private()
        self._protected()
        self.public()

        print(f"Fruit type: {fruit}")

    def __private(self) -> None:
        print("private: SuperClass")

    def _protected(self) -> None:
        print("protected: SuperClass")

    def public(self) -> None:
        """Function public() is accessible directly"""
        print("public(): SuperClass")

    # private copy of original public() method
    __public = public


class SubClass(SuperClass):
    """Class
    provides a new signature for public() but does not break __init__()"""

    def __init__(self) -> None:
        # The super() function is a built-in function that can be called inside
        # the derived class and gives access to the methods and variables of
        # the parent classes or sibling classes. Sibling classes are the
        # classes that share the same parent class. When you call the super()
        # function, you get an object that represents the parent class in
        # return.
        super().__init__("Apple")
        print("Apple is sweet")

    def public(self) -> None:
        print("public(): In SubClass")


def method_overriding() -> None:
    """Function demonstrates method overriding"""

    super_class_obj = SuperClass("Pineapple")
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


def inheritance() -> None:
    """Function demonstrate inheritance"""

    def built_in_functions() -> None:
        """Function Built-in functions"""
        # There are two built-in functions that can come in handy when trying to
        # find the relationship between different classes and objects:
        # issubclass() and isinstance().

        print(
            f"issubclass(SubClass, SuperClass) = {issubclass(SubClass, SuperClass)}"
        )  # issubclass(SubClass, SuperClass) = True
        print(
            f"issubclass(SuperClass, SubClass) = {issubclass(SuperClass, SubClass)}"
        )  # issubclass(SuperClass, SubClass) = False

        sub_class = SubClass()
        print("sub_class = SubClass()")
        print(f"isinstance(sub_class, SubClass) = {isinstance(sub_class, SubClass)}")

        fruit_apple = SubClass()
        print(isinstance(fruit_apple, SubClass))

    built_in_functions()
