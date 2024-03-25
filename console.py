#!/usr/bin/python3
"""Defines the HBNBCommand class, a command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program at End of File (EOF)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_help(self, arg):
        """Print help information"""
        if arg == "User":
            print("Supported commands:")
            print("\tcreate: Creates a new instance of User")
            print("\tshow: Prints the string representation of a
                  User instance")
            print("\tdestroy: Deletes a User instance")
            print("\tupdate: Updates attributes of a User instance")
            print("\tall: Prints all User instances")
        else:
            super().do_help(arg)

    def do_help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program")

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg == "User":
            new_user = User()
            new_user.save()
            print(new_user.id)
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
        else:
            super().do_create(arg)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg:
            class_name = arg.split()[0]
            if class_name not in self.classes():
                print("** class doesn't exist **")
                return
            objs = [str(obj) for key, obj in storage.all().items()
                    if isinstance(obj, self.classes()[class_name])]
        else:
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_objects[key], args[2], args[3])
        all_objects[key].save()

    def default(self, line):
        """Called on an input line when the comd prefix is not recognized."""
        print("")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
