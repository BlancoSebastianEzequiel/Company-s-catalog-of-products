import React from 'react'
import ModifyContainer from './ModifyContainer'
import PropTypes from 'prop-types'
import data from '../data/clientData'

export default class ModifyClientContainer extends React.Component {

  render () {
    return (
      <div>
        <ModifyContainer
          fields={data.fields}
          fieldsState={data.fieldsState}
          title='Modify client'
          objectName='client'
          endpoint='/users/'
          urlToRedirect='/client-list'
          id={this.props.location.state.id}
        />
      </div>
    )
  }
}

ModifyClientContainer.propTypes = {
  location: PropTypes.object
}
