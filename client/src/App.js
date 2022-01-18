import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([[[],[],[]]]);

  useEffect(() => {
    fetch("/members")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
      });
  },);

  return (
    <>
      <div>
          {data.map((item) => {
            var winner = "team1";
            if (item[2] === 0){
              winner = "team2";
            }
            var champImg = "champDefaultImg";
            return <div class={winner}>
              <img class={champImg} src={`/img/champion/tiles/${item[0][0]}_0.jpg`} alt={item[0][0]} ></img>
              <img class={champImg} src={`/img/champion/tiles/${item[0][1]}_0.jpg`} alt={item[0][1]} ></img>
              <img class={champImg} src={`/img/champion/tiles/${item[0][2]}_0.jpg`} alt={item[0][2]} ></img>
              <img class={champImg} src={`/img/champion/tiles/${item[0][3]}_0.jpg`} alt={item[0][3]} ></img>
              <img class={champImg} src={`/img/champion/tiles/${item[0][4]}_0.jpg`} alt={item[0][4]} ></img>
              <img class={champImg} src={`/img/champion/tiles/${item[1][0]}_0.jpg`} alt={item[0][0]} ></img>
              <img class={champImg} src={`/img/champion/tiles/${item[1][1]}_0.jpg`} alt={item[0][1]} ></img>
              <img class={champImg} src={`/img/champion/tiles/${item[1][2]}_0.jpg`} alt={item[0][2]} ></img>
              <img class={champImg} src={`/img/champion/tiles/${item[1][3]}_0.jpg`} alt={item[0][3]} ></img>
              <img class={champImg} src={`/img/champion/tiles/${item[1][4]}_0.jpg`} alt={item[0][4]} ></img>
            </div>;
          })}
      </div>
    </>
  );
}
//data.members.map((member, i) => <p key={i}>{member}</p>)
export default App;
