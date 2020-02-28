# message-builder-cli-app

## Instructions for how to run this program

### Requirements

- [Python3](https://www.python.org/downloads/)
- [pip3](https://pip.pypa.io/en/stable/installing/): pip is already installed if you are using Python 3 >=3.4 downloaded from [python.org](https://www.python.org)
- [git](https://git-scm.com/downloads)

### Install Required packages

Open terminal on your local machine and clone the repository to local machine.

```bash
git clone git@github.com:WHYjun/message-builder-cli-app.git
```

Change directory to the repository

```bash
cd message-builder-cli-app
```

Install the required packages to run this application

```bash
pip3 install -r requirements.txt
```

### Run Message Builder App

Start application. Once you start the application, please follow the instruction it gives.

```bash
python app/runner.py
```

## How to verify the correctness of this program

I added test cases in json file to verify the correctness of this program to fulfill the functional requirements and handle user inputs. My test plan was checking how this program handles invalid inputs from users, empty data in json file, and additional square brackets not used for placeholder.

During testing, I realized that I focused too much on the functional requirements and how to handle user inputs. I should have set up pytest to automate unit tests for each method to check it works correctly.

## An overview of design decision

I choose to use the Builder pattern to simplify the building process of Message objects. With this pattern, I can construct complex objects step by step regardless of how many new placeholders we will have later. Also, this pattern allows us to create different types and representations of Message objects using the same MessageBuilder class later. For example, I can change the current Message object to GreetingMessage object and create a parent Message class which can be inherited by GreetingMessage object, FarewellMessage object, PromotionMessage object and so on.

I create an abstract class Component for Guest, Company, and Template objects, because they have some common behaviors that can be inherited. At the same time, I can let other methods be instantiated in child class. For example, `print_list()` method should be instantiated by each subclass, because data in each json file is different from each other.

I intentionally make every property public to build this project quickly. To encapsulate the Message object perfectly, properties should be private and each class should have a getter/setter method. This can be one of future improvements in this project.

## Language I picked and why

I picked Python to build this project. I am quite familiar with working in Python and it is easy to create Command-line applications like this.

At first, I considered C# application, because I am currently using C# .Net Framework at work. However, I don't want to build an application which can be run Windows OS only.

## Future Improvements

1. As I mentioned above, I would like to automate testing to check each method works correctly whenever this project builds.
2. I want to add user verification on top of this project. Now, a user can access any data and send a message to any guest regardless of which hotel an user works. To do this, we should put our data into the database and create relationships among them.
3. I want users to save new guests and companies as they can save new message templates.
4. I want to clean up the `Message.populate()` method and try to separate each class. When I designed the project, it seemed better to have one generic method to populate data into a Message object, but it is actually not a better idea. If I have more time, I want to revisit this logic and redesign it.
