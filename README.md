



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTDHWEAA%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T070042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJGMEQCIDwA1r%2FTpRHwXoZ%2BN6%2BUFiGEBPYUA8dFIwVGQ8%2F0SFFPAiAHtUPcAxzynw1mtXxSQ76rZN9ow%2FgRpUUXKqFAdAlQqCqIBAjo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAqk6DQdLBbPJk%2BESKtwDB7kzgIyXTn8BpsvSxKnnGXv6GPgjxF1IGrg%2B46mrIo4VfZUFmvd5HG30QDAVQVEWfpDL8FNspHR8VcfO5bJS1CHswDSexAmDnhK4XQsB5HKZO8L%2F2ljFAhaoDUNT7e7ODXHYNcsunRCuG%2Fb9pTVxCh40hBNMyNb7DrrkSnljC1MigOzJQEvR6fE%2BLLn5HdbvMFVaUUlfV6cAdiPdHNLdnK6I4fVXuN9TNhuKo2nyPzeGYecBQ%2FaSdWstM2rBS19ywn6vXINNg%2FHEeSphkW01ZGV7eT9u3lEbfjV85KqRi1FMAfH5%2FQEthX%2FeRE87oSvOl1%2FzBKRwPnrJcXhCks3KsjIE6Du0xjWFpce6GBQFBQOrMHvh13J8a%2FmiC33SyV57KWf%2BQXXHkQuNpbipSL0NwOD2Czj%2BC9xkS8K1b451Ny1aLdXc3x3uyBFy0aMdh6v8LjCvWMVdifjL8l2XXEtQD9tuCLgzelXzey41PnIOJzxne6ycUShsxnknAkjX5bvywbRl3ZdHvJrEEoMjuhMsc6TS2VxaP27%2B5NvTeub%2BohLD4QSce7O2bgT1I5JMqRsyYAjghPTc8TIRxMkm%2B6zAWvwsKb31cKFuvwIwLYufImkFq5Bfh6n%2FY5ZCBKYwrMqMzwY6pgFtLqkhpP0u4LqQtOksM9yqMflWm3YYUBkIIwGm6qRhw4tfl1Kl1IM6oW7bGYHHQXNDPI5UTjsvsL5LdTQpx6q1HgmHy%2F%2Ba%2Bxw0nN2DdPNJ5U6LGAei5yTLtPrkZJMTGZ6k4iEliQlF7SBxXQSSq6yMjGGLTVntsE6eKVouYpfFaDMZm5koo%2BKG5reovT3GtFfAWUurotji2dmZhjrbp%2FUykLh4uLla&X-Amz-Signature=735bfa3186fda86afcf226925425cf0c5205c1a3d9ac3ab3602e076cfb2690cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTDHWEAA%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T070042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJGMEQCIDwA1r%2FTpRHwXoZ%2BN6%2BUFiGEBPYUA8dFIwVGQ8%2F0SFFPAiAHtUPcAxzynw1mtXxSQ76rZN9ow%2FgRpUUXKqFAdAlQqCqIBAjo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAqk6DQdLBbPJk%2BESKtwDB7kzgIyXTn8BpsvSxKnnGXv6GPgjxF1IGrg%2B46mrIo4VfZUFmvd5HG30QDAVQVEWfpDL8FNspHR8VcfO5bJS1CHswDSexAmDnhK4XQsB5HKZO8L%2F2ljFAhaoDUNT7e7ODXHYNcsunRCuG%2Fb9pTVxCh40hBNMyNb7DrrkSnljC1MigOzJQEvR6fE%2BLLn5HdbvMFVaUUlfV6cAdiPdHNLdnK6I4fVXuN9TNhuKo2nyPzeGYecBQ%2FaSdWstM2rBS19ywn6vXINNg%2FHEeSphkW01ZGV7eT9u3lEbfjV85KqRi1FMAfH5%2FQEthX%2FeRE87oSvOl1%2FzBKRwPnrJcXhCks3KsjIE6Du0xjWFpce6GBQFBQOrMHvh13J8a%2FmiC33SyV57KWf%2BQXXHkQuNpbipSL0NwOD2Czj%2BC9xkS8K1b451Ny1aLdXc3x3uyBFy0aMdh6v8LjCvWMVdifjL8l2XXEtQD9tuCLgzelXzey41PnIOJzxne6ycUShsxnknAkjX5bvywbRl3ZdHvJrEEoMjuhMsc6TS2VxaP27%2B5NvTeub%2BohLD4QSce7O2bgT1I5JMqRsyYAjghPTc8TIRxMkm%2B6zAWvwsKb31cKFuvwIwLYufImkFq5Bfh6n%2FY5ZCBKYwrMqMzwY6pgFtLqkhpP0u4LqQtOksM9yqMflWm3YYUBkIIwGm6qRhw4tfl1Kl1IM6oW7bGYHHQXNDPI5UTjsvsL5LdTQpx6q1HgmHy%2F%2Ba%2Bxw0nN2DdPNJ5U6LGAei5yTLtPrkZJMTGZ6k4iEliQlF7SBxXQSSq6yMjGGLTVntsE6eKVouYpfFaDMZm5koo%2BKG5reovT3GtFfAWUurotji2dmZhjrbp%2FUykLh4uLla&X-Amz-Signature=f14d0d2ade3c051ab9ae9800072583d739d3f0761a1ec97d7b6e0af4ad9990fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







