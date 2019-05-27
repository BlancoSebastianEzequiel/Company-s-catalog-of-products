import React from 'react'
import RegisterObjectContainer from './RegisterObjectContainer'
import data from '../data/contactUsData'

export default class ContactUsContainer extends React.Component {
  render () {
    return (
      <div>
        <RegisterObjectContainer
          fields={data.fields}
          fieldsState={data.fieldsState}
          title='Contact us'
          objectName='contact us'
          endpoint='/contact_us/'
          urlToRedirect='/'
        />
      </div>
    )
  }
}
