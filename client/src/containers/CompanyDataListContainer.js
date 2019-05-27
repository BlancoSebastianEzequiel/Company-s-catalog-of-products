import React from 'react'
import ListContainer from './ListContainer'

export default class CompanyDataListContainer extends React.Component {
  writeInfo = (data) => {
    let msg = ''
    for (let field in data) {
      if (field === '_id') continue
      msg += '__' + field + '__: ' + data[field] + '\n'
    }
    return {
      'data': msg,
      '_id': data['_id']
    }
  }

  render () {
    return (
      <div>
        <ListContainer
          url='/company_data/'
          query='/company_data/'
          writeInfo={(data) => this.writeInfo(data)}
          urlToRedirect='/modify-company-data'
          title='Company'
          dataName={'companyData'}
          showSearchNavBar={false}
        />
      </div>
    )
  }
}
