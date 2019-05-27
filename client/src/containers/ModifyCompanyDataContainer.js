import React from 'react'
import ModifyContainer from './ModifyContainer'
import PropTypes from 'prop-types'
import data from '../data/clientData'

export default class ModifyCompanyDataContainer extends React.Component {
  render () {
    return (
      <div>
        <ModifyContainer
          fields={data.fields}
          fieldsState={data.fieldsState}
          title='/company_data/'
          objectName='Company'
          endpoint='/company_data/'
          urlToRedirect='/company-data-list'
          id={this.props.location.state.id}
        />
      </div>
    )
  }
}

ModifyCompanyDataContainer.propTypes = {
  location: PropTypes.object
}
