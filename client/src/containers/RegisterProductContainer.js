import React from 'react'
import RegisterObjectContainer from './RegisterObjectContainer'
import data from '../data/productData'

export default class RegisterProductContainer extends React.Component {
  render () {
    return (
      <div>
        <RegisterObjectContainer
          fields={data.fields}
          fieldsState={data.fieldsState}
          title='Create new product'
          objectName='product'
          endpoint='/products/'
          urlToRedirect='/product-list'
        />
      </div>
    )
  }
}
