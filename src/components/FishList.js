import React from 'react';

export default function FishList(props) {

  return (
    <div>
      <h2>Fish List</h2>
      {props.fish[props.hemisphere].map(fish => fish.name)}
    </div>
  )
}
