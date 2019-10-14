import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.SwingUtilities;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.BorderFactory;

public class MyBrush_ver6 {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createGUI();
            }
        });
    }

    private static void createGUI() {
        JFrame f = new JFrame("My sad little brushy");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        MyBrushPanel panel1 = new MyBrushPanel();
        f.add(panel1);
        f.pack();
        f.setVisible(true);

        f.addKeyListener(new KeyAdapter() {

            public void keyPressed(KeyEvent e) {

                int key = e.getKeyCode();
                if (key == KeyEvent.VK_SPACE) {
                    panel1.clear();
                }
            }
        });
    }
}

class MyBrushPanel extends JPanel {

    private final ArrayList<Point> point = new ArrayList<>();

    public MyBrushPanel() {
        setBorder(BorderFactory.createLineBorder(Color.black));

        addMouseListener(new MouseAdapter() {
            public void mousePressed(MouseEvent e) {
                point.add(e.getPoint());
                repaint();
            }
        });

        addMouseMotionListener(new MouseAdapter() {
            public void mouseDragged(MouseEvent e) {
                point.add(e.getPoint());
                repaint();
            }
        });
    }

    public Dimension getPreferredSize() {
        return new Dimension(640, 480);
    }

    public void clear() {
        point.clear();
        repaint();
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Color aColor = new Color(0xFF0096);
        g.setColor(aColor);

        for (Point p : point) {
            g.fillOval(p.x, p.y, 4, 4);
        }
    }

}