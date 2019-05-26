import React from 'react'
import ListContainer from './ListContainer'

export default class ActivePrincipleListContainer extends React.Component {
  writeInfo = (anActivePrinciple) => {
    return {
      'data': 'CODE: ' + anActivePrinciple['code'] + ' -- NAME: ' + anActivePrinciple['name'],
      '_id': anActivePrinciple['_id']
    }
  }

  render () {
    return (
      <div>
        <ListContainer
          url='/active_principle/'
          query='/active_principle/'
          writeInfo={(anActivePrinciple) => this.writeInfo(anActivePrinciple)}
          urlToRedirect='/modify-active-principle'
          title='Active Principles'
          dataName={'activePrinciple'}
          showSearchNavBar={false}
        />
      </div>
    )
  }
}
