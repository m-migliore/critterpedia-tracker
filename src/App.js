import React, { useState, useEffect } from 'react';
import fishList from './python-scrapper/fish.json'
import bugsList from './python-scrapper/bugs.json'

import FishList from './components/FishList'

import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [currentMonth, setCurrentMonth] = useState("");
  const [currentHemisphere, setCurrentHemisphere] = useState("")
  const [fish, setFish] = useState(null)
  const [bugs, setBugs] = useState(null)
  const [fishReady, setFishReady] = useState(false)
  


  useEffect(() => {
    if (currentMonth === "") {
      let currentMonthInt = currentTime.getMonth()
      setCurrentMonth(getMonthName(currentMonthInt))
    }

    if (currentHemisphere === "") {
      navigator.geolocation.getCurrentPosition((data) => {
        data.coords.latitude > 0 ? setCurrentHemisphere("northern") : setCurrentHemisphere("southern")
      }, (data) => {debugger}, {enableHighAccuracy: true,timeout: 5000,maximumAge: 0});
    }

    setFish(fishList)
    setBugs(bugsList)

    if (!!fish && !!currentHemisphere && fishReady === false) {
      setFishReady(true)
    }

  }, [currentTime, currentMonth, currentHemisphere, fish, fishReady]);

  

  const getMonthName = (monthInt) => {
    let monthObj = {
      0: "January",
      1: "February",
      2: "March",
      3: "April",
      4: "May",
      5: "June",
      6: "July",
      7: "August",
      8: "September",
      9: "October",
      10: "November",
      11: "December"
    }

    return monthObj[monthInt]
  }

  return (
    <div className="App">
      <header className="App-header">
        Critterpedia Tracker
        {fishReady ? <FishList fish={fish} hemisphere={currentHemisphere}/> : "LoadingFish"}
      </header>
    </div>
  );
}

export default App;
