% rebase('base.tpl')

<h2>Veldu vöru í körfu!</h2>
<div>
    % for i in range(len(products)):
       <p> <a href="/cart/add/{{ products[i]["pid"] }}"> {{ products[i]["name"] }} </a> </p>
    % end
</div>
