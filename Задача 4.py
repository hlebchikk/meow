<html>
<head>
<title>Задача 4.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #7a7e85;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #2aacb8;}
.s4 { color: #6aab73;}
.s5 { color: #cf8e6d;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Задача 4.py</font>
</center></td></tr></table>
<pre><span class="s0">#Магазин с булочками :)</span>
<span class="s1">Bun_price </span><span class="s2">= </span><span class="s3">10</span>
<span class="s1">print</span><span class="s2">(</span><span class="s4">&quot;Hi! Buns cost 10 coins each. How many coins do you have?&quot;</span><span class="s2">)</span>
<span class="s1">C </span><span class="s2">= </span><span class="s1">int</span><span class="s2">(</span><span class="s1">input</span><span class="s2">(</span><span class="s4">&quot;Coin:&quot;</span><span class="s2">))</span>
<span class="s1">print</span><span class="s2">(</span><span class="s4">&quot;How many buns do you want to buy?&quot;</span><span class="s2">)</span>
<span class="s1">B </span><span class="s2">= </span><span class="s1">int</span><span class="s2">(</span><span class="s1">input</span><span class="s2">(</span><span class="s4">&quot;Buns:&quot;</span><span class="s2">))</span>
<span class="s1">BUNS </span><span class="s2">= (</span><span class="s1">C </span><span class="s2">&gt;= </span><span class="s1">B </span><span class="s2">* </span><span class="s3">10</span><span class="s2">) * </span><span class="s1">B</span>
<span class="s1">COIN </span><span class="s2">= (</span><span class="s1">C </span><span class="s2">- (</span><span class="s1">BUNS </span><span class="s2">* </span><span class="s3">10</span><span class="s2">))</span>
<span class="s1">print</span><span class="s2">(</span><span class="s4">f&quot;Now you have </span><span class="s5">{</span><span class="s1">BUNS</span><span class="s5">} </span><span class="s4">buns and </span><span class="s5">{</span><span class="s1">COIN</span><span class="s5">} </span><span class="s4">coins in your backpack!&quot;</span><span class="s2">)</span></pre>
</body>
</html>