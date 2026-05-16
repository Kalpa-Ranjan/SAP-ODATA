



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6V6YKXN%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T185721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIALHK2C1QQETpTkViUQjmfbmsUoFVsIRsHG8rW9ToOwIgfDkYx4FLstPTtUCsjUPZ2ePU1MM8ryLJdq73vNr%2BV7UqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNJvhWJut4c0HZvBbSrcA75Ta7WZohmR60IcHy82w1bOb2CQkxn5D%2BYLc1yblomYve9h0BggBiSRchFLIGO0McJgHjhATL%2FgcY2IgCWKdUxXlVTZvmAAeQJ8RlXkHhGjSJlWmJN04nx996bdmqDX0L1DAWfQuDaTTc5991u3r4U6gkTjlWA2sbkinzZGJHf22V85nyXZ38x6VrOaA6potupVDxwr9iSalLCDjtI4ApGRSR3T8W6fSa6oSEw7HgpPkeTlOurKrW0GbidL41LlgnmLsElOvTn1HwjsKmmGgBHrS2hNhOtk6fbpOwIWgvao%2Foyp1xGPp2pj7PVsqXQVmyGNuKtOmf0gjRfm0QDxKDTqgK8UQQeWyGupIlywjIny%2FRn4%2BDjVKNU7iyymqPEkOeFVbuuvahPL8Z%2FjAmf0GhmZyDhXvpCN60qlBGMMP93vVVeoszOUtvND9sB1BQ%2FPZFminubJnzLgaqDme4VmYstnAOpk70QLfCVGjlI8W7MH0irfdSf9qtJeMe9VKfmGD8y7Pdii39%2Bh5jfqanSBr5vEX0rl5%2FDUxCJgkm4vsxe3KG0HsYIzv74zdj6q7q58RBAAsqK%2BqhkKaAtrZE8LxjySLqIcPTKBeZanyKO9PaUA5hYGY5UTzqw8OP%2FVMMreotAGOqUB2iLd9eeFqVAVcFZWKbYYz7rqplsYyortH3bIHD6GeDWK8bTXOfZx0DuFwqZVybTqQGOTC3%2FtpYP5rCgA9VVx%2BGYUlqzJTK60fnd%2FRg9yF%2BxF9uDmPLFcKjVppPxJyAYyOngkUeM5BbYtXkI8%2BUmajpU96U2YQClsaNotPpYTKHkl1AbAOkM9ONRRC8S21QYBdNYUc80tPTAiHVM4s4LfIT%2FEDWd0&X-Amz-Signature=4c5e100b7598c22aa79bf2b8c9dc32e4d448231d426bf59daae9a24fc7f95091&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6V6YKXN%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T185721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIALHK2C1QQETpTkViUQjmfbmsUoFVsIRsHG8rW9ToOwIgfDkYx4FLstPTtUCsjUPZ2ePU1MM8ryLJdq73vNr%2BV7UqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNJvhWJut4c0HZvBbSrcA75Ta7WZohmR60IcHy82w1bOb2CQkxn5D%2BYLc1yblomYve9h0BggBiSRchFLIGO0McJgHjhATL%2FgcY2IgCWKdUxXlVTZvmAAeQJ8RlXkHhGjSJlWmJN04nx996bdmqDX0L1DAWfQuDaTTc5991u3r4U6gkTjlWA2sbkinzZGJHf22V85nyXZ38x6VrOaA6potupVDxwr9iSalLCDjtI4ApGRSR3T8W6fSa6oSEw7HgpPkeTlOurKrW0GbidL41LlgnmLsElOvTn1HwjsKmmGgBHrS2hNhOtk6fbpOwIWgvao%2Foyp1xGPp2pj7PVsqXQVmyGNuKtOmf0gjRfm0QDxKDTqgK8UQQeWyGupIlywjIny%2FRn4%2BDjVKNU7iyymqPEkOeFVbuuvahPL8Z%2FjAmf0GhmZyDhXvpCN60qlBGMMP93vVVeoszOUtvND9sB1BQ%2FPZFminubJnzLgaqDme4VmYstnAOpk70QLfCVGjlI8W7MH0irfdSf9qtJeMe9VKfmGD8y7Pdii39%2Bh5jfqanSBr5vEX0rl5%2FDUxCJgkm4vsxe3KG0HsYIzv74zdj6q7q58RBAAsqK%2BqhkKaAtrZE8LxjySLqIcPTKBeZanyKO9PaUA5hYGY5UTzqw8OP%2FVMMreotAGOqUB2iLd9eeFqVAVcFZWKbYYz7rqplsYyortH3bIHD6GeDWK8bTXOfZx0DuFwqZVybTqQGOTC3%2FtpYP5rCgA9VVx%2BGYUlqzJTK60fnd%2FRg9yF%2BxF9uDmPLFcKjVppPxJyAYyOngkUeM5BbYtXkI8%2BUmajpU96U2YQClsaNotPpYTKHkl1AbAOkM9ONRRC8S21QYBdNYUc80tPTAiHVM4s4LfIT%2FEDWd0&X-Amz-Signature=ddf75b3000a070826403df940b18f207e59a545be8c625f18008a6fc1ed95550&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







