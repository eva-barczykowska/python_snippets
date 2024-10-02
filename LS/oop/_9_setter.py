# Using the code snippet provided below, add a setter method named name.
# Then, rename kitty to 'Luna' and invoke greet again.

# class Cat:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     def greet(self):
#         print(f"Hello! My name is {self.name}!")
#
#
# kitty = Cat('Sophie')
# kitty.greet()


# Expected output:
# Hello! My name is Sophie!
# Hello! My name is Luna!

class Cat:
    def __init__(self, name):
        # self._name = name  # was before, changing _name to name in the constructor, doesn't call the setter at the time of initialization but will still cause issues if you use self.name later
        self.name = name  # changed _name to name in the constructor, ensures the setter is always invoked right away

    @property  # getter needs to be defined first in order to define setter
    def name(self):
        return self._name  # note the difference here, self._name is accessed through the getter

    # @name.setter  # decorator to make name a setter
    # def name(self, new_name):
    #     self._name = new_name  # setter method to update the value of self._name
    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Name cannot be empty!")
        self._name = new_name

    def greet(self):
        print(f"Hello! My name is {self.name}!")


kitty = Cat('Sophie')
kitty.greet()
kitty.name = ''  # rename kitty to 'Luna'
kitty.greet()

'''Setter method are defined using a decorator with the same name as the getter method, followed by .setter.
In our example, we've defined the setter method for name using the @name.setter decorator. The setter method
takes an additional parameter (besides self), which represents the new value to be assigned,
and updates the value of self._name.

Note that you must define a getter for the same instance variable first, by using the @property decorator.

With the setter method defined, we can assign a new value to the name attribute using the assignment operator:'''

# kitty.name = 'Luna'  # rename kitty to 'Luna'

'''The assignment invokes the setter method and updates the _name instance variable. 
When we call the greet method afterward, it uses the updated value of the name attribute.

It's worth noting that we changed self._name = name in __init__ to self.name = name.
This isn't strictly necessary but it ensures that the setter method is used to initialize the instance variable.
This minor change is only necessary when the setter needs to perform some sort of operation in addition to just setting 
the instance variable, but may also be used for consistency.'''

'''
from chatGPT
The lesson points out that in the constructor (__init__), the change from self._name = name to self.name = name
ensures that the setter method is invoked when the instance is initialized. This may seem minor,
but it can be important if the setter is doing additional work (e.g., validation, logging).

By using self.name = name in the constructor, the setter method is consistently used, even when the object is
being created, making the code more uniform.

Why Use the @property and Setter Methods?
The lesson focuses on using the @property decorator to define both getter and setter methods. The advantage of using @property with a setter is that it:

Encapsulates access to the attribute:
You can control how the attribute is accessed and modified, allowing you to implement additional logic, such as
validation or transformation of data, without exposing the internal details directly.

Keeps a simple interface:
You can access and modify the attribute as though it were a regular attribute, while still keeping the flexibility
to change how it’s handled internally.

For example, calling kitty.name = 'Luna' looks simple and direct, but behind the scenes, it triggers the setter method.

Specific answer why they changed self._name to self.name in the constructor:
--------------------------------------------------------------------------

The Two Approaches:
self._name = name:

This is a direct assignment to the private instance variable _name.
It bypasses any custom logic you might have in the setter method.

self.name = name:
This invokes the setter method for name. Instead of assigning the value directly to _name,
Python uses the @name.setter method to process and set the value.
This approach gives you control over how the value is set (e.g., validation, transformations).

Got it! Let's clarify the part where the lesson says:

### Why the Change?

In the constructor (`__init__`), originally you might have written `self._name = name` to directly assign the
`name` to the private attribute `_name`. However, by changing it to `self.name = name`,
you ensure that the **setter method** is invoked.

#### What Does This Mean in Practice?

- When you use `self.name = name`, you're **calling the setter** method you defined with `@name.setter`.
This allows any custom logic you put in the setter to be applied, even when the object is first created.
  
- If you just use `self._name = name`, the setter is **bypassed**, and no extra logic (such as validation or processing)
will happen.

### Example of Why It Matters:

Suppose your setter adds validation, like this:

```python
@name.setter
def name(self, new_name):
    if not new_name:
        raise ValueError("Name cannot be empty!")
    self._name = new_name
```

- **Using `self._name = name`**: The constructor will skip the validation because you're directly setting `_name`
without calling the setter.
  
- **Using `self.name = name`**: The constructor will invoke the setter, and the validation will be applied.
If the name is invalid (e.g., empty), an error will be raised immediately.

By changing to `self.name = name`, you ensure the setter logic is applied even during object creation.

### Summary:

- **`self._name = name`** directly sets the private attribute without any extra logic.
- **`self.name = name`** uses the setter method, which allows you to apply any custom logic or validation every time
the attribute is modified, including during initialization.

Clarifying the difference:.
Both self._name = name and self.name = name can result in an error if your setter logic includes validation that gets
invoked later.

The key difference is that self.name = name ensures the setter is always invoked right away,
while self._name = name doesn't call the setter at the time of initialization but will still cause issues if you use
self.name later.'''