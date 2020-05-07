<html>
<head>
<title>Recuperare i dati da un DB MySQL</title>
</head>
<body>

<table>
    <?php require_once '../core/core.php';   ?>
    <?php require_once '../core/tags.php';   ?>
    <?php $result = get_all_tags())          ?>
    <?php foreach($result as $value) { ?>
        <li><?php echo value;  ?></li>
    <?php }  ?>
</table>

</ul>
</body>
</html>