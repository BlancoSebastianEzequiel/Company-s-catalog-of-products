import React from 'react'
import { Col, Form, Grid, Row } from 'react-bootstrap'
import PropTypes from 'prop-types'

export default class DeleteClientForm extends React.Component {
  constructor (props) {
    super(props)
    this.state = {}
  }

  handleChange = (name, value) => {
    this.setState({
      [name]: value
    })
  }

  submit = (aClient) => {
    this.props.deleteClient(aClient)
  }

  showList () {
    return (
      <div>
        { this.props.clients.map((aClient, idx) =>
          <div className="panel panel-default" key={idx}>
            <div className="panel-heading">{aClient.client_data}</div>
            <button
              className="btn btn-default" type="submit" onClick={() => this.submit(aClient) }
            >Delete
            </button>
          </div>
        )}
      </div>
    )
  }

  render () {
    this.props.getClients()
    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={12} md={6} mdOffset={3}>
            <Form horizontal>
              { this.showList() }
            </Form>
          </Col>
        </Row>
      </Grid>
    )
  }
}

DeleteClientForm.propTypes = {
  getClients: PropTypes.func,
  deleteClient: PropTypes.func,
  errors: PropTypes.object,
  clients: PropTypes.array
}
