'use strict'

const User = use("App/Models/User");

class UserController
{
  async create({ request })
  {
    const data = request.only(["username", "email", "password"]);

    const CreateUser = await User.create(data);

    return CreateUser;
  }
}

module.exports = UserController
