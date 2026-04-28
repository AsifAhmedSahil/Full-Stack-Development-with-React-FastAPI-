import React from "react"
import { useEffect } from "react"
import axios from "axios"


const Home = () => {
    const fetchData = async ()=>{
    try {
      const response = await axios.get("http://127.0.0.1:8000/")
      console.log(response)
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(()=>{
    fetchData();
  },[])

  return (
    <div>
      Home
    </div>
  )
}

export default Home
