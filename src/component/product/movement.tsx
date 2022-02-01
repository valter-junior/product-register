import Cookies from "universal-cookie";
import { Component, useEffect, useState } from "react"
import axios, { AxiosRequestConfig } from 'axios'
import ReactTable from "react-table"; 
const baseUrl = "http://localhost:8000";

const cookies = new Cookies();

// get token generated on login
const token = cookies.get("token");

export default class Movement extends Component<any, any> {

    constructor(props){
        super(props)
        this.state = {
          movement: [],
          loading:true
        }
      }

      async getUsersData(){
        const res: AxiosRequestConfig = await axios({
          method: 'GET',
          url: `${baseUrl}/product/movement`,
          headers: {
            Authorization: `Berear ${token}`
          }
        })
        console.log(res.data)
        this.setState({loading:false, movement: res.data})
      }
      componentDidMount(){
        this.getUsersData()
      }
      render() {
        const columns = [{  
          Header: 'Name',  
          accessor: 'name' ,
          }
         
         ,{  
         Header: 'Purchase',  
         accessor: 'purchase' ,
         }
         ,{  
         Header: 'Sales',  
         accessor: 'sales',
         },
         {  
          Header: 'QtdStock',  
          accessor: 'qtdStock',
          },
          {  
            Header: 'Cost',  
            accessor: 'cost',
            },
          {  
            Header: 'Revenues',  
            accessor: 'revenues',
            },
          {  
            Header: 'Profit',  
            accessor: 'profit',
           }
            
      ]
        return (
          <ReactTable  
          data={this.state.movement}  
          columns={columns}  
       />
        )
      }
}
    



