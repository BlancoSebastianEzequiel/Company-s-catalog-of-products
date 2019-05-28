import React from 'react'
import ListContainer from './ListContainer'

export default class HelpModuleListContainer extends React.Component {
  writeInfo = (data) => {
    return {
      'data': '__Title__: ```' + data['title'] + '```__Description__: ```' + data['description'] + '```',
      '_id': data['_id']
    }
  }

  render () {
    return (
      <div>
        <ListContainer
          url='/help_module/'
          query='/help_module/'
          writeInfo={(data) => this.writeInfo(data)}
          urlToRedirect='/modify-help-module'
          title='Help Module'
          dataName={'helpModule'}
          showSearchNavBar={false}
        />
      </div>
    )
  }
}
