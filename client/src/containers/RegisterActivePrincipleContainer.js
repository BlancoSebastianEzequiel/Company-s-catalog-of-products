import React from 'react'
import RegisterObjectContainer from './RegisterObjectContainer'
import data from '../data/activePrincipleData'

export default class RegisterActivePrincipleContainer extends React.Component {
  render () {
    return (
      <div>
        <RegisterObjectContainer
          fields={data.fields}
          fieldsState={data.fieldsState}
          title='Create new active principle'
          objectName='active principle'
          endpoint='/active_principle/'
          urlToRedirect='/active-principle-list'
        />
      </div>
    )
  }
}
