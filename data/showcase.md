{% for scope in data|sort %}

## {{scope.title}}

{% for type in scope.types|sort(attribute='title') %}
<div class="card">
  <div class="text">
    <h3><a href="{{type.url}}">{{type.title}}</a></h3>
    <p>{{type.summary}}</p>
    <p><a href="{{type.download}}">Download as .zip</a>
  </div>
</div>
{% endfor %}

{% endfor %}
