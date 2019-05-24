import React from 'react'
import ModifyContainer from './ModifyContainer'
import PropTypes from 'prop-types'
import data from '../data/activePrincipleData'

export default class ModifyActivePrincipleContainer extends React.Component {
  render () {
    return (
      <div>
        <ModifyContainer
          fields={data.fields}
          fieldsState={data.fieldsState}
          title='Modify active principle'
          objectName='active principle'
          endpoint='/active_principle/'
          urlToRedirect='/active-principle-list'
          id={this.props.location.state.id}
        />
      </div>
    )
  }
}

ModifyActivePrincipleContainer.propTypes = {
  location: PropTypes.object
}
