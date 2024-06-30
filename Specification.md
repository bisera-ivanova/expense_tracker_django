This API should let you:

Sign up as a new user.
Generate and validate JWT tokens for handling authentication and user session.
List and filter your past expenses
Add new expenses.
Remove existing expenses.
Update existing expenses.
Let’s now add some constraints:

You’ll be using JWT (JSON Web Token) to protect the endpoints and to identify the requester.
For the different expense categories, you can use the following list (feel free to decide how to implement this as part of your data model):
Groceries
Leisure
Electronics
Utilities
Clothing
Health
Others.
As a recommendation, you can use MongoDB or an ORM for this project, such as Mongoose (if you’re using JavaScript/Node for this).

