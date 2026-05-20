import { useState } from "react";

import {
  useNavigate,
  Link
} from "react-router-dom";

import api from "../api/api";


export default function Register() {

  const navigate = useNavigate();

  const [username, setUsername] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");


  const registerUser = async () => {

    try {

      await api.post(
        "/auth/register",
        {
          username,
          email,
          password,
        }
      );

      alert("Registration successful");

      navigate("/");

    } catch (error) {

      console.error(error);

      alert("Registration failed");
    }
  };


  return (

    <div className="min-h-screen bg-slate-900 flex justify-center items-center">

      <div className="bg-slate-800 p-10 rounded-2xl w-[400px]">

        <h1 className="text-3xl text-white font-bold mb-8">
          Register
        </h1>

        <input
          type="text"
          placeholder="Username"
          className="w-full p-4 rounded-lg mb-4"
          value={username}
          onChange={(e) =>
            setUsername(e.target.value)
          }
        />

        <input
          type="email"
          placeholder="Email"
          className="w-full p-4 rounded-lg mb-4"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full p-4 rounded-lg mb-4"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button
          onClick={registerUser}
          className="w-full bg-green-600 hover:bg-green-700 text-white p-4 rounded-lg font-bold"
        >
          Register
        </button>

        <p className="text-white mt-4 text-center">

          Already have an account?

          <Link
            to="/"
            className="text-blue-400 ml-2"
          >
            Login
          </Link>

        </p>

      </div>

    </div>
  );
}
