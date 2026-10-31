



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KRW6YBU%2F20261031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261031T120600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD91g1KsZS%2BPwNAgw9MFieKM8uhgatV33xK9Iv0shvk%2BgIhANZ7qX2c675vtSO5SA0UDmSoB8xjJI6vYswMXoTE3E2OKv8DCEsQABoMNjM3NDIzMTgzODA1IgyZabyCac5Jc7e2Nf8q3AMNjsCw9gvbfWQuV7Y3wWDI0GC7nTrnnuugO3UTDnnbjpwOVh1YGcv5fWrYSsJlvjN1gIjIaOrvEPE%2FbQsftnF8P49Y95SMtmk3LAq1Kf%2BFu9bR%2BcG80AbBy96tWPzlv3nsdDHUYyldprz7Dl7wg1ZP8Qgm3G5%2FSWFqxhvc4syZNdAgDavV%2BBBpOzR3MH31TNvvoQ%2BcQ87c8QRptBMd5wesRksV7kez8I0J0Nqy0J0h9bEWQr08ADBLlv81wKeSzlPR9zpVbtSx5mG61YoTd2gv3z%2FIvgOgVZbqObvFS156qnPvQYiEknWPoyBYSCtbKa361E2dBBo%2FK20qGihZ1aE50Qesf0za0FZ%2BEKqi%2BSaKM0gDgxujUk4GVNL8jSxnqXtwMLHeojSGgN1ASCVd1hw52%2BQWVhuEs1QiXKB2ChRGEvvmPBBv2gGaRMso2YuOr%2BT%2BKKH5H4eARIdSrsj4zZNUkhccfDs7i5qIG0uu0eb9mJg0vsiUsm1vVtpTCqN0n2bPolUrRc4G2uqfpDQmZdYfbnDcXwQua7xASseMAxifYI0o3sXXBCQVRE%2FdMzHq8M4u3mKG%2F1JF2bcUzraDwy5jIS6X8%2FenoXD06hWvUuSEH5r7VMNjcZm2Fjq%2FlTCVi5fXBjqkARzhcwdjniqJCXU7jB07CMJZmBaq5CdfA4QN8yPwho7ygyYsUyc6%2FQ1eEovqqD0ksUpeH1L2WilvczDQoLxy7fqJQ8sPqrt%2BFnp8NVr8KcI0j5uSjZxGQEpbSELL6hMkl%2FpXcKNBpni4l2vazSb8N2YrQPgpu29IqE%2BHAAetgdtHnaUHdjPcy5qGtlV5rj0dEBanDdE6hSGERqcvA8qL0%2FXwEkT3&X-Amz-Signature=3dc12cdb81c8576b423039d956f2e7ec5be2e9114e8c4d3ba009f2145a20e2cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KRW6YBU%2F20261031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261031T120600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD91g1KsZS%2BPwNAgw9MFieKM8uhgatV33xK9Iv0shvk%2BgIhANZ7qX2c675vtSO5SA0UDmSoB8xjJI6vYswMXoTE3E2OKv8DCEsQABoMNjM3NDIzMTgzODA1IgyZabyCac5Jc7e2Nf8q3AMNjsCw9gvbfWQuV7Y3wWDI0GC7nTrnnuugO3UTDnnbjpwOVh1YGcv5fWrYSsJlvjN1gIjIaOrvEPE%2FbQsftnF8P49Y95SMtmk3LAq1Kf%2BFu9bR%2BcG80AbBy96tWPzlv3nsdDHUYyldprz7Dl7wg1ZP8Qgm3G5%2FSWFqxhvc4syZNdAgDavV%2BBBpOzR3MH31TNvvoQ%2BcQ87c8QRptBMd5wesRksV7kez8I0J0Nqy0J0h9bEWQr08ADBLlv81wKeSzlPR9zpVbtSx5mG61YoTd2gv3z%2FIvgOgVZbqObvFS156qnPvQYiEknWPoyBYSCtbKa361E2dBBo%2FK20qGihZ1aE50Qesf0za0FZ%2BEKqi%2BSaKM0gDgxujUk4GVNL8jSxnqXtwMLHeojSGgN1ASCVd1hw52%2BQWVhuEs1QiXKB2ChRGEvvmPBBv2gGaRMso2YuOr%2BT%2BKKH5H4eARIdSrsj4zZNUkhccfDs7i5qIG0uu0eb9mJg0vsiUsm1vVtpTCqN0n2bPolUrRc4G2uqfpDQmZdYfbnDcXwQua7xASseMAxifYI0o3sXXBCQVRE%2FdMzHq8M4u3mKG%2F1JF2bcUzraDwy5jIS6X8%2FenoXD06hWvUuSEH5r7VMNjcZm2Fjq%2FlTCVi5fXBjqkARzhcwdjniqJCXU7jB07CMJZmBaq5CdfA4QN8yPwho7ygyYsUyc6%2FQ1eEovqqD0ksUpeH1L2WilvczDQoLxy7fqJQ8sPqrt%2BFnp8NVr8KcI0j5uSjZxGQEpbSELL6hMkl%2FpXcKNBpni4l2vazSb8N2YrQPgpu29IqE%2BHAAetgdtHnaUHdjPcy5qGtlV5rj0dEBanDdE6hSGERqcvA8qL0%2FXwEkT3&X-Amz-Signature=75f74cc7fc9be0f54528156c3c90101cd68b9d23ca1ac912651cc453c853478d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







