



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCGN42HW%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T180543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAkjaPtZU%2FOcON9O05oGPsqPOPsZMSgO75MvyUuZPU1%2BAiAYUr4c6sJL%2Bz2pMY2RVJ9E9mazgyiabTf33sIUn4AjSSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM1wwqEFChZIicz%2BxgKtwD%2BIj%2F1c2J8p75uJHetFdjaoBtEljQ3V12Q4bq33OQx6hwsTEZ3Aj9uGM7t7QG57RByeSSrkLCZZtCYZpxkC3ca5BDTufG1Jp6XfBQZYBkmRbY3%2F%2BZjeXCkhQ7VXdzNHMBLII4suliFzuj6OZaf0iFikxcob4pkkZkiLwEr0Phmkgz0bcjUW%2BacJsM7tawAhJv4rXpRs4DNuZhFASqq4cUt%2FoNvW%2Btfs17TrD212LM%2B7dV2zQdvUJU%2BdABQtSU1j0MQlOeqV3bf%2BHeKOMhtpxTy50rE0muOfSY1kNWZ47DKnKyO12W2KDeysYvSTvJRp094kO2ezC4dnSWNQorkTXk7nU6yEAemOQvjQlArxu9Tq0omaBN1FNeFqbFvNinqygi3yuCtdR68zS9mExjfhrxz%2FSLENw1ljhnWsR6D2plnYKo%2FfXj%2BgLJM5onk1AL0NHia8SF8Tks6mNQM%2BRl7b0I8TXVP9awQRIOo%2Bwv0n8vqjmErM8QRNtjNQ1qe%2FLXC0l5MDgu55ZEdPr64S2q74940HCV6jkIVrhm4XSTDa7Cn18hBkFcU0D0GF%2BOywVbreqomPyX1ecVl7OoMwmIBU3G1I5bhrLO1WT1ixZ8pPAmmQdo7ttW2qb8J29fTDEwiOyR2AY6pgFJd1YGPdUFs7Y6LyyWrgTDSq2xGLZmuqNV56O0GjoMhnQ3XcF8Fzmbmc4VoskLpoeyAoabqmh3hYC7xwm%2FNI9HZYfgZaxWcfXa1yKqYcpfrEhTKUiokeU6VQ3uJRPOkwP7lms5d8033TgZKLvGRJeIS8EoeeLQyrx9gmBThxvj7jboOXbQIGq6fww8KghslhWwXAdCE602RHiYnC7UPDcaCI%2BIkEps&X-Amz-Signature=67bba15472359fe63c9c6068a36954cf6ed0564a57345fa2a0519b36ea3cab3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCGN42HW%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T180543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAkjaPtZU%2FOcON9O05oGPsqPOPsZMSgO75MvyUuZPU1%2BAiAYUr4c6sJL%2Bz2pMY2RVJ9E9mazgyiabTf33sIUn4AjSSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIM1wwqEFChZIicz%2BxgKtwD%2BIj%2F1c2J8p75uJHetFdjaoBtEljQ3V12Q4bq33OQx6hwsTEZ3Aj9uGM7t7QG57RByeSSrkLCZZtCYZpxkC3ca5BDTufG1Jp6XfBQZYBkmRbY3%2F%2BZjeXCkhQ7VXdzNHMBLII4suliFzuj6OZaf0iFikxcob4pkkZkiLwEr0Phmkgz0bcjUW%2BacJsM7tawAhJv4rXpRs4DNuZhFASqq4cUt%2FoNvW%2Btfs17TrD212LM%2B7dV2zQdvUJU%2BdABQtSU1j0MQlOeqV3bf%2BHeKOMhtpxTy50rE0muOfSY1kNWZ47DKnKyO12W2KDeysYvSTvJRp094kO2ezC4dnSWNQorkTXk7nU6yEAemOQvjQlArxu9Tq0omaBN1FNeFqbFvNinqygi3yuCtdR68zS9mExjfhrxz%2FSLENw1ljhnWsR6D2plnYKo%2FfXj%2BgLJM5onk1AL0NHia8SF8Tks6mNQM%2BRl7b0I8TXVP9awQRIOo%2Bwv0n8vqjmErM8QRNtjNQ1qe%2FLXC0l5MDgu55ZEdPr64S2q74940HCV6jkIVrhm4XSTDa7Cn18hBkFcU0D0GF%2BOywVbreqomPyX1ecVl7OoMwmIBU3G1I5bhrLO1WT1ixZ8pPAmmQdo7ttW2qb8J29fTDEwiOyR2AY6pgFJd1YGPdUFs7Y6LyyWrgTDSq2xGLZmuqNV56O0GjoMhnQ3XcF8Fzmbmc4VoskLpoeyAoabqmh3hYC7xwm%2FNI9HZYfgZaxWcfXa1yKqYcpfrEhTKUiokeU6VQ3uJRPOkwP7lms5d8033TgZKLvGRJeIS8EoeeLQyrx9gmBThxvj7jboOXbQIGq6fww8KghslhWwXAdCE602RHiYnC7UPDcaCI%2BIkEps&X-Amz-Signature=8575f139a70ac30271b59103896f87e28ee733a2cb6fb653fa920aa54fa38395&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







