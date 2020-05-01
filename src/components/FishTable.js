import React, { useState, useEffect } from 'react';
import FishTableRow from './FishTableRow'

export default function FishList(props) {

  // const [fishRowsReady, setFishRowsReady] = useState(false)

  // useEffect(() => {
  //   if (!!fish && !!currentHemisphere && fishReady === false) {
  //     setFishReady(true)
  //   }

  // }, [fishRowReady]);

  return (
    <div>
      <h2>Fish List</h2>
      <table>
        <thead>
          <tr>
            {Object.keys(props.fish[props.hemisphere][0]).map(rowTitle => <th>{rowTitle}</th>)}
          </tr>
        </thead>
        <tbody>
          {props.fish[props.hemisphere].map(fish => <FishTableRow rowData={fish} />)}
        </tbody>
      </table>
    </div>
  )
}
