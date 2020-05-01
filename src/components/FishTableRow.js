import React from 'react'

const renderFishData = (fishData) => {
  return Object.keys(fishData).map(key => {
      if (key === "image") {
        return <td><img src={fishData[key]} alt={fishData["name"]}/></td>
      } else {
        return <td>{fishData[key]}</td>
      }
    })
}

export default function FishTableRow(props) {
  return (
    <tr>
      {renderFishData(props.rowData)}
    </tr>
  )
}
