import React from 'react'
import ListContainer from './ListContainer'

export default class ClientListContainer extends React.Component {
  writeInfo = (aProduct) => {
    let msg = ''
    for (let field in aProduct) {
      if (field === '_id') continue
      msg += '__' + field + '__: ```' + aProduct[field] + '```'
    }
    return {
      'data': msg,
      '_id': aProduct['_id']
    }
  }

  render () {
    return (
      <div>
        <ListContainer
          url='/products/'
          query='/products/'
          writeInfo={(aProduct) => this.writeInfo(aProduct)}
          urlToRedirect='/modify-product'
          title='Products'
          dataName={'product'}
          showSearchNavBar={true}
        />
      </div>
    )
  }
}
