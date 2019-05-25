import React from 'react'
import ListContainer from './ListContainer'

export default class ClientListContainer extends React.Component {
  writeInfo = (aProduct) => {
    return {
      'data': 'Code: ' + aProduct['code'] + ' -- Name: ' + aProduct['name'],
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
        />
      </div>
    )
  }
}
