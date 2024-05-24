public class TriangleTester {
    public enum Kind {
        SCALENE,
        ISOSCELES,
        EQUILATERAL,
        BADSIDE,
        NOTRIANGLE
    }

    public static Kind triangleTest(int s1, int s2, int s3) {
        if (s1 <= 0 || s2 <= 0 || s3 <= 0)
            return Kind.BADSIDE;
        else if (s1 + s2 <= s3 || s2 + s3 <= s1 || s1 + s3 <= s2)
            return Kind.NOTRIANGLE;
        else if (s1 == s2 && s2 == s3)
            return Kind.EQUILATERAL;
        else if (s1 == s2 || s2 == s3 || s1 == s3)
            return Kind.ISOSCELES;
        else
            return Kind.SCALENE;
    }

    public static void main(String[] args) {
        int side1 = 4;
        int side2 = 4;
        int side3 = 4;
        Kind triangleKind = triangleTest(side1, side2, side3);
        System.out.println("Triangle kind: " + triangleKind);
    }
}
