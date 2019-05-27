import React from 'react'
import RegisterObjectContainer from './RegisterObjectContainer'
import data from '../data/helpModuleData'

export default class RegisterHelpMofuleContainer extends React.Component {
  render () {
    return (
      <div>
        <RegisterObjectContainer
          fields={data.fields}
          fieldsState={data.fieldsState}
          title='Create new product'
          objectName='help module'
          endpoint='/help_module/'
          urlToRedirect='/help-module-list'
        />
      </div>
    )
  }
}
