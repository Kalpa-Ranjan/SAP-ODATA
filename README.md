



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZIWVGJ5%2F20261112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261112T001254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4CAIpHHVKimQ6UX19zEH1Am3Fwgww3ZyWj7X1CMdBpAIhALB1zrBRFqCEU7EkvwcAvQaXKnk0lecLYsvbD4mjqoDdKv8DCF8QABoMNjM3NDIzMTgzODA1IgxUiKNQee5pgpcbKeAq3APy8tF5Dd67MbawWLZy9eLfzcDljjyaVpCAYy4Gay36pgSKJErlJnbWMbas%2Fl7%2BTmSvJqPN8FSMWHL47%2B7cwCkkmG%2B%2FwQ9WgXyiELB2%2FuXdGQablUfhMvVYGpRmXNwLDFS93k1LZADy316WRLPdswJj5ZHbrBpj2%2BSeP3FFh9hFCtljHZLYy3Gvs8yCpmblhzsmQUyencUI%2FNi6RTx95Hu08LWqfviKon1h7LmYLZP0pkYCccvtvsUkD8q6OnGxXkNqc5RE2svYHBGrcQNYLCe0XDBx%2FdVG91QF9l5gW0HqxlKikx0F9hRvJVHy1akz0kQTSmkL%2BDZyuz4%2FBf8TRSANYUCj3kdYGy1LpCSUuhRkY3nyOsjUHJsX%2FfqJiI4aWjEXkR1wXes5JssOOdFRM%2FImrr386LZFhAc0z36x3sw%2BO1IMDuzLD%2Fta6pYlK4EC%2BRC1vuIToyTpDyULGjfNuQZI1qvNKhysmsdpd%2BCVuEzdTPtTthwTErplUmHvV2WI%2BA0SHDHFRyZgoD%2F%2Br0VOPCxzBExO%2FzOy2JFfYlnCunbB1I3TSP55PqlXIfk%2Fxpub8R0cgEwx7GvrG4wiRILBasGoh11%2BMEzn%2BzOKyopKp3J86PajUMlNHkmCbrDOvTDv19PXBjqkAVndYveUih5Cnl9GMkagxTNkNbkseODKwMQTeYigfmRbnDNXjzPyMKj78hvPHOKYx014p%2FJgmotCC18Tnmfv%2BNcLBD7dGhIZkEuF7AHbsq8uE4lxjJaLh4w%2FrpYQFKJ5eNTJWXqKp4QzcRJDL5vKZTJWsytxk0g2N4z%2Bag5jvdoT%2BtxKP57O02LD4vewk%2B7ky5XgO2OHaaj2V97v69bZStIlcUMP&X-Amz-Signature=b6380812472a29f491c523926d4268db49865e89946be5543cc7a8b71758df75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZIWVGJ5%2F20261112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261112T001255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4CAIpHHVKimQ6UX19zEH1Am3Fwgww3ZyWj7X1CMdBpAIhALB1zrBRFqCEU7EkvwcAvQaXKnk0lecLYsvbD4mjqoDdKv8DCF8QABoMNjM3NDIzMTgzODA1IgxUiKNQee5pgpcbKeAq3APy8tF5Dd67MbawWLZy9eLfzcDljjyaVpCAYy4Gay36pgSKJErlJnbWMbas%2Fl7%2BTmSvJqPN8FSMWHL47%2B7cwCkkmG%2B%2FwQ9WgXyiELB2%2FuXdGQablUfhMvVYGpRmXNwLDFS93k1LZADy316WRLPdswJj5ZHbrBpj2%2BSeP3FFh9hFCtljHZLYy3Gvs8yCpmblhzsmQUyencUI%2FNi6RTx95Hu08LWqfviKon1h7LmYLZP0pkYCccvtvsUkD8q6OnGxXkNqc5RE2svYHBGrcQNYLCe0XDBx%2FdVG91QF9l5gW0HqxlKikx0F9hRvJVHy1akz0kQTSmkL%2BDZyuz4%2FBf8TRSANYUCj3kdYGy1LpCSUuhRkY3nyOsjUHJsX%2FfqJiI4aWjEXkR1wXes5JssOOdFRM%2FImrr386LZFhAc0z36x3sw%2BO1IMDuzLD%2Fta6pYlK4EC%2BRC1vuIToyTpDyULGjfNuQZI1qvNKhysmsdpd%2BCVuEzdTPtTthwTErplUmHvV2WI%2BA0SHDHFRyZgoD%2F%2Br0VOPCxzBExO%2FzOy2JFfYlnCunbB1I3TSP55PqlXIfk%2Fxpub8R0cgEwx7GvrG4wiRILBasGoh11%2BMEzn%2BzOKyopKp3J86PajUMlNHkmCbrDOvTDv19PXBjqkAVndYveUih5Cnl9GMkagxTNkNbkseODKwMQTeYigfmRbnDNXjzPyMKj78hvPHOKYx014p%2FJgmotCC18Tnmfv%2BNcLBD7dGhIZkEuF7AHbsq8uE4lxjJaLh4w%2FrpYQFKJ5eNTJWXqKp4QzcRJDL5vKZTJWsytxk0g2N4z%2Bag5jvdoT%2BtxKP57O02LD4vewk%2B7ky5XgO2OHaaj2V97v69bZStIlcUMP&X-Amz-Signature=56e623658990c688ded24f09547773645af6beaadc5e376cabf369f1e5075184&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







