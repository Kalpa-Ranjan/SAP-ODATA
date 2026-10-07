



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ43TTZ2%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T002322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDkFQUfX9QIOGVhqr7HL3I2vfC%2Frlk%2Bhy%2FTYaoR%2FsTaKAiBf2RoRJ%2Fr%2BScQO%2BU4LvT5240%2BSD3l%2B7go0pbdZJfkjBSr%2FAwgAEAAaDDYzNzQyMzE4MzgwNSIMAfpn%2BQgWygVSvxQiKtwDUxAnYWPUT%2Bfvoz24%2FNwSFpG4MA5mE29O9knptOKIPtO0VPXmXFo8gyIZu4s%2Bfgpt%2B7u%2Fam6hCleee5CYsE6sR%2BwoDAQ%2BSNIfnb%2BlnnUCTJsqeJnQHMOoOWviK6sGRc4cmwM7uN6PHFhONYU382zir7ybS1pDXzF92X1L94YdkSQ4iu4f%2F2QmuzO9QMSU%2Fq6ZTBd8XjvjSReJVg0GofwApS1OulqmeS%2F4jm2afFeGdHZtWA7tGWvL608WjE8Y6DC5FnBauvqspO9K6LalruqoedtEpOMFDIG0eW8UwDuCUFnYFdLGdU%2BEtyWdHJSkSh9M32zBXbysc%2Br2ZSaLNXzJk0dLxFiDVwXtToqBTutK2yq6U%2FcwLIVCKgppaQY8FEhNgcyiVUJ0ndv0LQrDf%2Bj3eYO7WsX9d9rJDs8bmeJHYTkUL6Ims5syWAep7hO3qkjjEAuP9mcgQbyeDkSGdnDc3DqiPu7YyWBc7u9P5eyJ47m%2FfIKyetqhERraAScLKlwVaaIja%2BigB4%2BQZ8A83wTnE1aMm7rBULyL11vlVOaF1xD5En%2FkAZFLFwhguDF5ByOIyIvWFyZATXctXOJqmvrW8rQm13xy%2FGtHMAfbHYro5fvGPTHEw2UeQb%2B79%2F0wkomW1gY6pgHTap5agyuNMvEFAJNFoITsMww1sjDdewFxjQe6LmzfhdgPNM1nBkPpXs5FzpkaMqTipZX3A993uQZleTk%2FW9%2FyzuSbHxw1MZiXxTmeytD7xu%2Ba02RWM0BgKnt6mZ4I2PtwOQNBJPhNFZA2bz74BgUuhg681tuiY9oZucI9qYGfnC0MmG90w%2B0KZJvoffmcpe2QHCRE57lwtWHdOCaRteo8KP6jT2Dv&X-Amz-Signature=215effc31ec2df3fa379cb6a3cfc243d16c409d71dc03b7f4224eb6080ec8e59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ43TTZ2%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T002323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDkFQUfX9QIOGVhqr7HL3I2vfC%2Frlk%2Bhy%2FTYaoR%2FsTaKAiBf2RoRJ%2Fr%2BScQO%2BU4LvT5240%2BSD3l%2B7go0pbdZJfkjBSr%2FAwgAEAAaDDYzNzQyMzE4MzgwNSIMAfpn%2BQgWygVSvxQiKtwDUxAnYWPUT%2Bfvoz24%2FNwSFpG4MA5mE29O9knptOKIPtO0VPXmXFo8gyIZu4s%2Bfgpt%2B7u%2Fam6hCleee5CYsE6sR%2BwoDAQ%2BSNIfnb%2BlnnUCTJsqeJnQHMOoOWviK6sGRc4cmwM7uN6PHFhONYU382zir7ybS1pDXzF92X1L94YdkSQ4iu4f%2F2QmuzO9QMSU%2Fq6ZTBd8XjvjSReJVg0GofwApS1OulqmeS%2F4jm2afFeGdHZtWA7tGWvL608WjE8Y6DC5FnBauvqspO9K6LalruqoedtEpOMFDIG0eW8UwDuCUFnYFdLGdU%2BEtyWdHJSkSh9M32zBXbysc%2Br2ZSaLNXzJk0dLxFiDVwXtToqBTutK2yq6U%2FcwLIVCKgppaQY8FEhNgcyiVUJ0ndv0LQrDf%2Bj3eYO7WsX9d9rJDs8bmeJHYTkUL6Ims5syWAep7hO3qkjjEAuP9mcgQbyeDkSGdnDc3DqiPu7YyWBc7u9P5eyJ47m%2FfIKyetqhERraAScLKlwVaaIja%2BigB4%2BQZ8A83wTnE1aMm7rBULyL11vlVOaF1xD5En%2FkAZFLFwhguDF5ByOIyIvWFyZATXctXOJqmvrW8rQm13xy%2FGtHMAfbHYro5fvGPTHEw2UeQb%2B79%2F0wkomW1gY6pgHTap5agyuNMvEFAJNFoITsMww1sjDdewFxjQe6LmzfhdgPNM1nBkPpXs5FzpkaMqTipZX3A993uQZleTk%2FW9%2FyzuSbHxw1MZiXxTmeytD7xu%2Ba02RWM0BgKnt6mZ4I2PtwOQNBJPhNFZA2bz74BgUuhg681tuiY9oZucI9qYGfnC0MmG90w%2B0KZJvoffmcpe2QHCRE57lwtWHdOCaRteo8KP6jT2Dv&X-Amz-Signature=233623081a679e0a019bbd4c95708f61b094abbab13d074f376a2645bf6d26cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







