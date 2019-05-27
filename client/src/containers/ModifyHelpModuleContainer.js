import React from 'react'
import ModifyContainer from './ModifyContainer'
import PropTypes from 'prop-types'
import data from '../data/helpModuleData'

export default class ModifyHelpModuleContainer extends React.Component {
  render () {
    return (
      <div>
        <ModifyContainer
          fields={data.fields}
          fieldsState={data.fieldsState}
          title='Modify help module'
          objectName='help module'
          endpoint='/help_module/'
          urlToRedirect='/help-module-list'
          id={this.props.location.state.id}
        />
      </div>
    )
  }
}

ModifyHelpModuleContainer.propTypes = {
  location: PropTypes.object
}
