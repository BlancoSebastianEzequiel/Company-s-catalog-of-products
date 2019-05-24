import React from 'react'
import ListContainer from './ListContainer'

export default class ClientListContainer extends React.Component {
  writeInfo = (aClient) => {
    return {
      'data': 'USER NAME: ' + aClient['user_name'] + ' -- EMAIL: ' + aClient['email'],
      '_id': aClient['_id']
    }
  }

  render () {
    return (
      <div>
        <ListContainer
          url='/users/'
          query='/users/?type=client'
          writeInfo={(aClient) => this.writeInfo(aClient)}
          urlToRedirect='/modify-client'
        />
      </div>
    )
  }
}
