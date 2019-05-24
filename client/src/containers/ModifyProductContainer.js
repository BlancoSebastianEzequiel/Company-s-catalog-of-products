import React from 'react'
import ModifyContainer from './ModifyContainer'
import PropTypes from 'prop-types'
import data from '../data/productData'

export default class ModifyProductContainer extends React.Component {
  render () {
    return (
      <div>
        <ModifyContainer
          fields={data.fields}
          fieldsState={data.fieldsState}
          title='Modify product'
          objectName='product'
          endpoint='/products/'
          urlToRedirect='/product-list'
          id={this.props.location.state.id}
        />
      </div>
    )
  }
}

ModifyProductContainer.propTypes = {
  location: PropTypes.object
}
