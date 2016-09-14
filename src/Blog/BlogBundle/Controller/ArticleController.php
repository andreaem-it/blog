<?php
namespace Blog\BlogBundle\Controller;

use Symfony\Component\HttpFoundation\Response;

class ArticleController
{
    public function indexAction($limit)
    {
        return new Response(
            '<html><body>Numero: '.rand(1,100).'</body></html>'
        );
    }
}
?>