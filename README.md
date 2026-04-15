



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUAPVP6H%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T190848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YesJYNO9ZZ1LCV6uUJB9uuSL97wpwBllkfjuEsnQswIgMLElP0Lc4GezMflEQLIwe9zWcYI9XEYyBMMUH6qOchAqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBVcff3R1to0XiZ9JircA%2FrHjtE4Hngb9EWVPB3xp58oL2m7n9wLGppCbYB5X1S5n2zbzGpv0PHF8hWFv8BBEHcgAWcNYxwK3MSbyS%2FxMtoJVp978mESVqDe%2BL97mWlLs4a1s4IM5T%2F%2FN10%2B1SrOCrZeB5MZzQAU9EbtwdIJp7HnrNuls15BqWj%2FR8WvGD%2FDLe2ugCPz4FQJoNrXIH2JZmP%2BOOnFNBK3gUSzIJjyVCfpt9zq%2FHfRehudXJbS8EBv3S9VbKxgu2yblnWdB%2B5PyUf2iz1wlJZH93Qck%2F0rOCQ3OwWGdpH8AmbEyMOVwJGx4ZZiew%2Fh8N1R9PoHUDCZLnw5Oe5ckQQ3la36TMUad8%2BUuh%2BST9ukU4FQHXTubWKAVTRv1RHKCPZPn5gvPyDQaK5yZWxaDFH%2BQjfzHaDX%2BHEoT44k6tWpj3IdZMTbMPvnzmbHLB7T2RciE853x4o1oC2TD8%2B%2Bj2TdIODxhQmIkK8IwAUVW%2B%2F8IKCBn2FPySEBIN2U3woCs2NdKEPnExxL6MVvwHnDJEx%2Ff%2BqiE34pI64M%2BpH65M5dWepkAlT81C9T0hLCnnFDra5v0bX3rc59U8ljYO4IXu%2BFymtjue5uvazi58dfZjtTPHDojLsjjJbJ8c0LJ9tIi4uiwQKoMN%2BS%2F84GOqUB%2Ft%2FvVRY233l42%2B1Oj4gIG8sYzMOBBsKEIsKymiCr41xpPj9k%2FpoY6%2Fy1nlhii3gQoh57ftTKn4Qsf4RCYEF1yKsl6QuPSz2PrCRn%2B%2Fw6f%2BMD2oiRJx%2FWQO82ldFl%2B5X9vzUXX50tBxVpJVivHuTSQ89Gs3M4q4TH8AUeDnWM8eWp7j2kXQKRgjo3Q3NdtsmyDcTdjaXdTl5CXTNCrf%2Fq1kc4sc%2BJ&X-Amz-Signature=4f961e5fecdcbb57cd2b6310290fff615a76f8d2e7a27009df1b954d0e899830&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUAPVP6H%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T190848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YesJYNO9ZZ1LCV6uUJB9uuSL97wpwBllkfjuEsnQswIgMLElP0Lc4GezMflEQLIwe9zWcYI9XEYyBMMUH6qOchAqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBVcff3R1to0XiZ9JircA%2FrHjtE4Hngb9EWVPB3xp58oL2m7n9wLGppCbYB5X1S5n2zbzGpv0PHF8hWFv8BBEHcgAWcNYxwK3MSbyS%2FxMtoJVp978mESVqDe%2BL97mWlLs4a1s4IM5T%2F%2FN10%2B1SrOCrZeB5MZzQAU9EbtwdIJp7HnrNuls15BqWj%2FR8WvGD%2FDLe2ugCPz4FQJoNrXIH2JZmP%2BOOnFNBK3gUSzIJjyVCfpt9zq%2FHfRehudXJbS8EBv3S9VbKxgu2yblnWdB%2B5PyUf2iz1wlJZH93Qck%2F0rOCQ3OwWGdpH8AmbEyMOVwJGx4ZZiew%2Fh8N1R9PoHUDCZLnw5Oe5ckQQ3la36TMUad8%2BUuh%2BST9ukU4FQHXTubWKAVTRv1RHKCPZPn5gvPyDQaK5yZWxaDFH%2BQjfzHaDX%2BHEoT44k6tWpj3IdZMTbMPvnzmbHLB7T2RciE853x4o1oC2TD8%2B%2Bj2TdIODxhQmIkK8IwAUVW%2B%2F8IKCBn2FPySEBIN2U3woCs2NdKEPnExxL6MVvwHnDJEx%2Ff%2BqiE34pI64M%2BpH65M5dWepkAlT81C9T0hLCnnFDra5v0bX3rc59U8ljYO4IXu%2BFymtjue5uvazi58dfZjtTPHDojLsjjJbJ8c0LJ9tIi4uiwQKoMN%2BS%2F84GOqUB%2Ft%2FvVRY233l42%2B1Oj4gIG8sYzMOBBsKEIsKymiCr41xpPj9k%2FpoY6%2Fy1nlhii3gQoh57ftTKn4Qsf4RCYEF1yKsl6QuPSz2PrCRn%2B%2Fw6f%2BMD2oiRJx%2FWQO82ldFl%2B5X9vzUXX50tBxVpJVivHuTSQ89Gs3M4q4TH8AUeDnWM8eWp7j2kXQKRgjo3Q3NdtsmyDcTdjaXdTl5CXTNCrf%2Fq1kc4sc%2BJ&X-Amz-Signature=b1fdf3d0499e33a32341fe10f8f819ce548be432875b34905106ed196248671e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







