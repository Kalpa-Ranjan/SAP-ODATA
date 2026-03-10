



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKWFH3A2%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T125105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQCz8MqIIGBWgvaEK0O%2BP7eQz6EDBLzS7MZC8HElqYiVXgIhALe%2BNSIEjpv1HhtXbCANstKQ3DlwGpmoOoBK8FKG7oUFKv8DCEUQABoMNjM3NDIzMTgzODA1IgzkRGqaCtJs%2B0%2Fp7lYq3AMM2w6U7GBadvW%2FHZUBXt1yodzmBVzBr9PT4u32iQ%2FzkWiMu3gv%2BOOQqmb4px386FN31i8hMy9TP3OrspaZXQoXo%2BpspdKr1IRVuHbODz8sj6J9lkt1nZKO5B%2B6lYRxhZoJCMEGNWAGNk06kFLS0RW80MKC1RcUBJ6k9I7uEi8Klb2mbwwawvWWJRJ1QRpsyxksQmu0r26sg2%2FiQ64f%2BAMIIsNdORDgP%2FCmhVNvkNrZPH%2FMqPXXOC7M3wVCY0c9VGX17Jq%2FioU7VHRaMDLHxsbhokER%2Fc9aEG1TlEGVnVRVmCGrETlIln%2BcRp0rwZDQft%2B0Ecb9CUe%2FnzaHlqI2rSp4XS4tsk6AJUkK2eWsR0hLfRx1WWVpNZLQNdmxKmiHbQsEio6iwBUD9UNhkeGtFASIttayc99zGikARQRJUPafGmqqITJ150SkB2cPB4M2FEeriTGOoTE00aLfVUlDiAkSyAZwKG%2FzSvVdsCysEZDmEJmt19lx%2F4XOhd3jnPalCqt42jPIv1DXQBPfqAycfP9RpyPO7CgPunmnJfvlG3de4VwbMvPj5srvt94FA8LbnwPSlP91X0Ux5WJm9orlBrt4Ag9l0rRC1RVyO0rAaJ%2FR4VZO6JcEGOVkDmNMuzD%2FhMDNBjqkAV6UQKx6RauQMuEaAOkOBhSHTXu147vtyIo3G0mtHw2DuNFtVYIATR862%2FdOR0RQHwveDgTn7OvOOnicqHhajpsOL2vYCYJpUaH6cPYArO6jWewEXz6Fra6Qm%2FvvpMEWdbXdfJYnl66dEveuGYB6o5XapWJcccmdcbWj12BWcSxY0v0tcJXYREu85nJZDsfmROsQ0tw7D%2B%2FOlqmGaHfXnAvMn10y&X-Amz-Signature=288c02ff8f9dba3dbd8b58b2e80b443d504331e4be5ca4365fa690a0af042e4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKWFH3A2%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T125105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQCz8MqIIGBWgvaEK0O%2BP7eQz6EDBLzS7MZC8HElqYiVXgIhALe%2BNSIEjpv1HhtXbCANstKQ3DlwGpmoOoBK8FKG7oUFKv8DCEUQABoMNjM3NDIzMTgzODA1IgzkRGqaCtJs%2B0%2Fp7lYq3AMM2w6U7GBadvW%2FHZUBXt1yodzmBVzBr9PT4u32iQ%2FzkWiMu3gv%2BOOQqmb4px386FN31i8hMy9TP3OrspaZXQoXo%2BpspdKr1IRVuHbODz8sj6J9lkt1nZKO5B%2B6lYRxhZoJCMEGNWAGNk06kFLS0RW80MKC1RcUBJ6k9I7uEi8Klb2mbwwawvWWJRJ1QRpsyxksQmu0r26sg2%2FiQ64f%2BAMIIsNdORDgP%2FCmhVNvkNrZPH%2FMqPXXOC7M3wVCY0c9VGX17Jq%2FioU7VHRaMDLHxsbhokER%2Fc9aEG1TlEGVnVRVmCGrETlIln%2BcRp0rwZDQft%2B0Ecb9CUe%2FnzaHlqI2rSp4XS4tsk6AJUkK2eWsR0hLfRx1WWVpNZLQNdmxKmiHbQsEio6iwBUD9UNhkeGtFASIttayc99zGikARQRJUPafGmqqITJ150SkB2cPB4M2FEeriTGOoTE00aLfVUlDiAkSyAZwKG%2FzSvVdsCysEZDmEJmt19lx%2F4XOhd3jnPalCqt42jPIv1DXQBPfqAycfP9RpyPO7CgPunmnJfvlG3de4VwbMvPj5srvt94FA8LbnwPSlP91X0Ux5WJm9orlBrt4Ag9l0rRC1RVyO0rAaJ%2FR4VZO6JcEGOVkDmNMuzD%2FhMDNBjqkAV6UQKx6RauQMuEaAOkOBhSHTXu147vtyIo3G0mtHw2DuNFtVYIATR862%2FdOR0RQHwveDgTn7OvOOnicqHhajpsOL2vYCYJpUaH6cPYArO6jWewEXz6Fra6Qm%2FvvpMEWdbXdfJYnl66dEveuGYB6o5XapWJcccmdcbWj12BWcSxY0v0tcJXYREu85nJZDsfmROsQ0tw7D%2B%2FOlqmGaHfXnAvMn10y&X-Amz-Signature=edc5f9f73bea9e7f40b412d714279d092fd518141645a5cd793fea2851016341&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







