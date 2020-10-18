# About

We will be building an API using the Django framework with DRF integrated, while explaining some of the components of these two frameworks. We are going to implement the views using the different ways presented by DRF to see how each one can be used.

# Todo API

This will be a simple API that have the following endpoints
- Fetch the list of all todos
- Create a new todo item
- Fetch an existing todo item
- Update an exisiting todo item
- Delete an existing todo item

While building out the above endpoints, we will ensure the following
- Implement identity and access management
- Write meaningful request tests
- Responses have the same top level structure
- Views does not include business logic
- Use the concept of actions for business logic

# Resources

DRF Documentation<br>
https://www.django-rest-framework.org/

Used Sections of the Documentation
- Quick Start Tutorial
- API Guides

# Steps

- Setup the development environment
- Use environment variables for some settings with python-decouple
- Register applications `rest_framework` and `api`
- Run migrations
- Define all models and run migrations [*]
- Create the list all todos endpoint
- Create the action package for business logics

# Folder Structure

### bin/

This folder is expected to contain bash script to help make running commands in the project easy and possible from the root directory. You can ignore this folder if you don't want to use the scripts or if its not compatible with your platform.

### project/

This is where all Django codes and components will go. This is the top level Django instance folder, which will contain the Django configuration modules, applications and other support modules and packages

Contrary to the way Django names the project folder and the folder for holding configuration scripts upon creation, I have subjectively decided to name the root Django project folder `project` and the folder containing configuration scripts `config`. This means naming the folders based on their purpose as opposed to the product.

The project has been generically divided into the parts that may or may not depend on one another
- Business
- Library
- Interfaces

### project/app

This is the `Business` part of the whole structure. This is an actual Django application that will have to be registered on the project. We can say that this application will only be responsible for managing data and how these data will be manipulated, hence the models and actions.

### project/lib

This is the `Library` part of the whole structure. This is where all reusable and non-business logic codes used across all application will live. This is not a Django application, but will have to be taken along with applications that uses codes from here.

### project/{interfaces}

Interfaces are components of the projects that will solely be responsible for receiving client requests, deligating the handling to an `app` action, generating a response from the output of the action and returning response back to the client.

These interface will simply just define necessary views and url mappings making up the interface endpoints. The currently implemented interfaces within this project includes
- api

# Components

From here down this README.md file are notes taken on the different components of DRF while building out this project. The explanations below is to give quick insights into what is available within DRF.

# Serializers

# Renderers

# Parsers

# View

# APIView

# ViewSet

# Action Mixins

# GenericAPIView

# Concrete Generic API Views

# GenericViewSet

# Concrete Generic ViewSets

# Pagination

# Authentication

# Authorization

# Browsable API

# Unit Tests

# Request Tests
